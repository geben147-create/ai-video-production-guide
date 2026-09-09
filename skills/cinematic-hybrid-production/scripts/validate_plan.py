"""Validate plan structure and timeline/allocation, never render quality or billing.

Usage: python validate_plan.py plan.json
Dependency: python -m pip install jsonschema
"""
import argparse
import json
import math
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator
except ImportError:
    raise SystemExit("Install the validation dependency: python -m pip install jsonschema")

SCHEMA = Path(__file__).resolve().parents[1] / "references" / "plan.schema.json"


def reject_constant(value):
    raise ValueError(f"Non-finite JSON number: {value}")


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"), parse_constant=reject_constant)


def validate(plan):
    errors = []
    warnings = []
    validator = Draft202012Validator(load_json(SCHEMA))
    for error in validator.iter_errors(plan):
        location = "/".join(str(x) for x in error.absolute_path) or "root"
        errors.append(f"{location}: {error.message}")
    if errors:
        return {"valid": False, "errors": errors, "warnings": warnings}

    policy = plan["policy"]
    scenes = plan["scenes"]
    ids = [s["frame_id"] for s in scenes]
    if len(ids) != len(set(ids)):
        errors.append("Duplicate frame_id values")
    missing = set(policy["protected_video_ids"]) - set(ids)
    if missing:
        errors.append("Unknown protected_video_ids: " + ", ".join(sorted(missing)))
    if policy["image_eligible_from_seconds"] > policy["total_seconds"]:
        errors.append("Image eligibility boundary exceeds total duration")

    elapsed = 0.0
    video_count = 0
    video_seconds = 0.0
    units = 0
    for index, scene in enumerate(scenes):
        sid = scene["frame_id"]
        start = scene["start_seconds"]
        duration = scene["duration_seconds"]
        if not math.isclose(start, elapsed, abs_tol=1e-6, rel_tol=0):
            errors.append(f"{sid}: timeline gap, overlap, or incorrect order at {start}; expected {elapsed}")
        for field in ("start_seconds", "duration_seconds"):
            frames = scene[field] * policy["fps"]
            if not math.isclose(frames, round(frames), abs_tol=1e-5, rel_tol=0):
                errors.append(f"{sid}: {field} is not aligned to the configured fps")
        elapsed = start + duration
        protected = scene["highlight"] or sid in policy["protected_video_ids"]
        is_video = scene["mode"] == "generated_video"
        if protected and not is_video:
            errors.append(f"{sid}: protected highlight must remain generated_video")
        if not is_video and start < policy["image_eligible_from_seconds"] - 1e-6:
            errors.append(f"{sid}: photo motion is before the allowed late section")
        if is_video:
            minimum = math.ceil(duration / policy["generation_clip_seconds"] - 1e-9)
            if scene["generation_units"] < minimum:
                errors.append(f"{sid}: needs at least {minimum} planned generation units")
            video_count += 1
            video_seconds += duration
        units += scene["generation_units"]
        if scene["transition"] == "actual_end_chain":
            if index == 0 or scene["predecessor"] != ids[index - 1]:
                errors.append(f"{sid}: physical continuation must reference the immediate preceding scene")

    if not math.isclose(elapsed, policy["total_seconds"], abs_tol=1e-6, rel_tol=0):
        errors.append(f"Timeline ends at {elapsed}, declared total is {policy['total_seconds']}")
    actual_ratio = video_count / len(scenes)
    if abs(actual_ratio - policy["target_video_scene_ratio"]) > 0.05 + 1e-9:
        warnings.append("Video scene ratio differs from the advisory target by more than five percentage points; explain it without downgrading protected scenes")
    return {
        "valid": not errors,
        "errors": errors,
        "warnings": warnings,
        "summary": {
            "scenes": len(scenes),
            "video_scenes": video_count,
            "photo_scenes": len(scenes) - video_count,
            "video_scene_ratio": round(actual_ratio, 6),
            "video_seconds": round(video_seconds, 6),
            "photo_seconds": round(policy["total_seconds"] - video_seconds, 6),
            "video_time_ratio": round(video_seconds / policy["total_seconds"], 6),
            "planned_generation_units": units,
            "actual_submission_count": "not checked; use execution log",
            "declared_total_seconds": policy["total_seconds"],
        },
        "scope": "Plan only. Does not verify assets, rendered frames, output continuity, rights, or current zero-credit quotes.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", type=Path)
    args = parser.parse_args()
    try:
        result = validate(load_json(args.plan))
    except (OSError, ValueError) as error:
        result = {"valid": False, "errors": [str(error)]}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    sys.exit(main())
