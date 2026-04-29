class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def Dhyan(idx, target, path):
            if target == 0:
                res.append(path[:])
                return

            for i in range(idx, len(candidates)):
                # skip duplicates
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                
                if candidates[i] > target:
                    break

                path.append(candidates[i])
                Dhyan(i + 1, target-candidates[i], path)
                path.pop()

        Dhyan(0, target, [])
        return res
        