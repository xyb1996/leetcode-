"""问题描述:
在D塔2这款游戏中，英雄和小兵都可以对对方的防御塔造成伤害，但是只有当对敌方防御塔最后的伤害是由英雄造成时，
才会得到相应的金钱奖励。  现在小明正在玩D塔2，操作英雄带着一波兵进入了对方的塔下进行攻击。
已知：  1. 一共有n个小兵，小兵的攻击力为d，所有小兵对塔的攻击是同时进行的，小兵的攻击冷却为t0。
  2. 小明的英雄有一个技能可以对塔造成伤害，伤害值为x；英雄的普通攻击也可以对塔造成的伤害，伤害值为y。
  小明的英雄普通攻击的冷却为t1，技能冷却为t2。  3. 小兵的攻击，小明的普通攻击和小明的技能攻击，
  只要冷却时间一到，就会马上攻击；小明的普通攻击和技能攻击可以同时施展；如果小兵和英雄同时攻击，小兵的伤害算在前。
  已知现在对方的塔还剩下s的血量，所有小兵的第一次攻击和英雄的第一次普通攻击和技能攻击在初始时刻同时进行，
  问小明可以得到破坏该塔的金钱奖励么？  注意：这里冷却是指连续两次攻击之间的等待时间
英雄的普通攻击和技能攻击的冷却两者互不干预。如果冷却是1，某次攻击发生在时间2，那么时间3才可以继续攻击。假定攻击立即生效。

输入：第一行一个整数T，表示测试组数，1≤T≤10；

接下来一行一个整数s，表示塔的剩余血量，1≤s≤10000；

接下来一行4个整数n,d,x,y，含义如题面，1≤n,d,x,y≤100；

接下来一行3个整数t0,t1,t2,含义如题面，1≤t0,t1,t2≤100。

输出：对于每组测试数据输出”YES”表示小明的英雄可以补到，”NO”表示不能。（输出不包括引号）

"""


t= int(input())
while True:
	try:
		s= int(input())
		#n个小兵，攻击力为d， x，技能攻击，y：普通攻击
		n, d, x, y = [int(i) for i in input().split()]
		#普通攻击冷却t1，技能冷却t2
		t0, t1, t2 = [int(i) for i in input().split()]

		count = 0
		flag = 0

		while s>0:
			if count % t0==0:
				s-=(n*d)
			if s <=0:
				break
			if count %t1 ==0:
				s-=y
			if count % t2 ==0:
				s-=x
			if s<=0:
				flag = 1
			count+=1

		if flag ==1:
			print('YES')
		else:
			print('NO')

	except:
		break


def get_money(blood):
	res = []
	s1, s2, s3 = 0, 0, 0
	while blood > 0:
		if s1 <= s2 and s1 <= s3:
			s1 += t0
			blood -= n * d
			res.append(0)
		elif s1 > s2 and s2 <= s3:
			s2 += t1
			blood -= y
			res.append(1)
		elif s1 > s3 and s2 >= s3:
			s3 += t2
			blood -= x
			res.append(1)
	return True if res[-1] == 1 else False


if __name__ == '__main__':
	m = int(input())
	for _ in range(m):
		blood = int(input())
		n, d, x, y = list(map(int, input().split()))
		t0, t1, t2 = list(map(int, input().split()))
		if get_money(blood):
			print('YES')
		else:
			print('NO')
