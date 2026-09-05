
document.querySelectorAll('.audit-tools,.filters').forEach(group=>{
  const buttons=[...group.querySelectorAll('.filter')];
  const section=group.closest('section');
  buttons.forEach(button=>button.addEventListener('click',()=>{
    buttons.forEach(b=>{b.classList.toggle('active',b===button);b.setAttribute('aria-pressed',String(b===button));});
    const choice=button.dataset.filter;
    section.querySelectorAll('.audit-row,.matrix-row').forEach(row=>row.classList.toggle('hidden',choice!=='all'&&row.dataset.status!==choice));
  }));
});
document.querySelectorAll('.copy').forEach(button=>button.addEventListener('click',async()=>{
  const target=document.getElementById(button.dataset.copy||'masterPrompt')||document.getElementById('promptText');
  if(!target)return;
  const label=button.textContent;
  try{if(!navigator.clipboard)throw new Error('Clipboard unavailable');await navigator.clipboard.writeText(target.textContent);button.textContent='복사 완료 ✓';}
  catch{const range=document.createRange();range.selectNodeContents(target);const selection=window.getSelection();if(selection){selection.removeAllRanges();selection.addRange(range);}button.textContent='선택 완료 · Ctrl+C로 복사';}
  window.setTimeout(()=>{button.textContent=label;},2400);
}));
const boxes=[...document.querySelectorAll('#qcGrid input[type=checkbox]')];
const progress=document.getElementById('progress')||document.getElementById('progressText');
if(boxes.length){
  const key='public-video-guide-qc-'+boxes.length;
  let saved=[];try{const parsed=JSON.parse(localStorage.getItem(key)||'[]');if(Array.isArray(parsed))saved=parsed;}catch{}
  const update=()=>{const state=boxes.map(b=>b.checked);try{localStorage.setItem(key,JSON.stringify(state));}catch{}if(progress)progress.textContent=state.filter(Boolean).length+' / '+boxes.length+' 완료';};
  boxes.forEach((box,i)=>{box.checked=saved[i]===true;box.addEventListener('change',update);});update();
}
