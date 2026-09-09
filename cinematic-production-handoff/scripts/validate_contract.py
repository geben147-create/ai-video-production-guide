import json, sys
def free(q):
 a=q.get('activityInfo',{})
 return type(q.get('discountCost')) in (int,float) and q['discountCost']==0 and type(a.get('discountCredit')) in (int,float) and a['discountCredit']==0 and a.get('activityMode')=='unlimited'
def gate(quotes): return len(quotes)==2 and all(free(q) for q in quotes)
if __name__=='__main__':
 good={'discountCost':0,'activityInfo':{'discountCredit':0,'activityMode':'unlimited'}}
 assert gate([good,good])
 assert not gate([good,{}])
 assert not gate([good,{'discountCost':15,'activityInfo':{'discountCredit':15,'activityMode':'unlimited'}}])
 assert not gate([good])
 print('Cost gate checks passed. Freshness and exact-request hashes must be checked by the submitting adapter.')
