while True:
	try:
		offset,n,lenL1,lenL2 = list(map(int,input().split()))
		start1,end1,start2,end2 =-1,-1,-1,-1
		if offset >= lenL1:
			start1 = end1 = lenL1
			start2 = min(offset - lenL1,lenL2)
			end2 = start2+n
			end2 = min(end2,lenL2)

		else:
			start1 = offset
			if start1+n>lenL1:
				end1 = lenL1
				start2 = 0
				end2 = n-(lenL1-offset)
			else:
				end1 = start1+n
				start2 = end2 = 0
		print(start1,end1,start2,end2,sep=' ')
	except:
		break


