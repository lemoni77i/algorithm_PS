import heapq

if __name__ == "__main__":
	min_val = -1000
	dx = [0, -1, 0, 1]
	dy = [-1, 0, 1, 0]

	t = int(input())	
	while t > 0:
		n = int(input())

		stickers = []
		d = [[0 for _ in range(3)] for _ in range(n)]

		t -= 1

		for i in range(2):
			stickers.append([int(x) for x in input().split(" ")])

		d[0][0]=0
		d[0][1]=stickers[0][0]
		d[0][2]=stickers[1][0]

		for i in range(1, n):
			d[i][0] = max(d[i-1][0], d[i-1][1], d[i-1][2])
			d[i][1] = max(d[i-1][0], d[i-1][2]) + stickers[0][i]
			d[i][2] = max(d[i-1][0], d[i-1][1]) + stickers[1][i]

		print(max(d[n-1][0], d[n-1][1], d[n-1][2]))