class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        piles.sort()
        alice_count = 0 
        bob_count = 0
        for i in range(len(piles)):
            if i % 2 == 0:
                alice_count += piles[i]
            else:
                bob_count += piles[i]
        
        if alice_count > bob_count:
            return False
    
        return True

