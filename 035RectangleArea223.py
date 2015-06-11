class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
		if G <= A or C <= E or D <= F or H <= B:##there is no intersection
			return (C-A)*(D-B) + (G-E)*(H-F)
		if A <= E and B <= F and C >= G and D >= H:##one rectangle is inside of another one
			return (C-A)*(D-B)
		xx = sorted([A,C,E,G])## there is a intersection
		yy = sorted([B,D,F,H])
		width = xx[2]-xx[1]
		heigt = yy[2]-yy[1]
		area = (C-A)*(D-B) + (G-E)*(H-F) - width*heigt
		return area
		
	def computeArea(self, A, B, C, D, E, F, G, H):
		overlay = min(D-B, H-F, max(D-F,0), max(H-B,0)) * min(C-A, G-E, max(C-E,0), max(G-A,0))
		return (C-A)*(D-B) + (G-E)*(H-F) - overlay
a = -2
b = -2
c = 2
d = 2
e = 1
f = -3
g = 3
h = -1
m = Solution()
n = m.computeArea(a,b,c,d,e,f,g,h)
print n
