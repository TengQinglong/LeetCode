#
# @lc app=leetcode.cn id=782 lang=python3
#
# [782] 变为棋盘
#

# @lc code=start
class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        #无解
        noAns=9999
        #计算需要移动的函数 与三叶不同的是 我把t放在外面
        def getCnt(x:int):
            cnt1,cnt2=0,0
            for i in range(n):
                cnt1+=((x>>i)&1)
                cnt2+=((t>>i)&1)
            if cnt1!=cnt2:return noAns
            return int(bin(x^t).count("1")/2)
        #定义初始化 两个不同的行 两个不同列
        r1,r2,c1,c2=-1,-1,-1,-1
        n=len(board)
        #构建mask 即全为1的行列值
        mask=(1<<n)-1
        #遍历原有棋盘 生成 r1 r2 c1 c2
        for i in range(n):
            a,b=0,0
            for j in range(n):
                if board[i][j]==1:a|=(1<<j)
                if board[j][i]==1:b|=(1<<j)
            if r1==-1:r1=a
            elif a!=r1 and r2==-1:r2=a
            if c1==-1:c1=b
            elif b!=c1 and c2==-1:c2=b
            if a!=r1 and a!=r2:return -1
            if b!=c1 and b!=c2:return -1
        #判断 r1和r2 是否符合要求 
        # if bin(r1).count("1")+bin(r2).count("1")!=n:return -1
        # if bin(c1).count("1")+bin(c2).count("1")!=n:return -1
        #此处与三叶不同 无需判断 1的个数和是否等于 nn
        #因为 异或运算包含了 判断 如果个数相加少于或者大于 异或结果必定不可能全部都是1
        if r1^r2!=mask or c1^c2!=mask:return -1
        #构建棋盘应该的样子
        t=0
        for i in range(0,n,2):t+=(1<<i)
        #分别计算 r1 r2 变成棋盘需要的步骤 取min值
        #计算 c1 c2 变成棋盘需要的步骤 取min值 相加为结果
        ans=min(getCnt(c1),getCnt(c2))+min(getCnt(r1),getCnt(r2))
        #如果ans >=noAns 说明不能构造 返回 -1
        if ans >=noAns:ans =-1
        return ans
        
# @lc code=end

