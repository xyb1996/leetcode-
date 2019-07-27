"""题目描述:
在你的每个回合开始时你可以选择以下两个动作之一：聚力或者攻击。
    聚力会提高你下个回合攻击的伤害。
    攻击会对敌人造成一定量的伤害。如果你上个回合使用了聚力，那这次攻击会对敌人造成buffedAttack点伤害。否则，会造成normalAttack点伤害。
给出血量HP和不同攻击的伤害，buffedAttack和normalAttack，返回你能杀死敌人的最小回合数。
"""
"""输入：第一行是一个数字HP
第二行是一个数字normalAttack
第三行是一个数字buffedAttack

输出：轮数
"""
import math
hp = int(input().strip())
normalattack = int(input().strip())
bufferattack= int(input().strip())
result = 0
if 2*normalattack >= bufferattack:
	result = math.ceil(hp / normalattack)
else:
	result += hp // bufferattack *2
	hp = hp % bufferattack
	if 0<hp <=normalattack:
		result +=1
	elif hp > normalattack:
		result+=2
print(result)