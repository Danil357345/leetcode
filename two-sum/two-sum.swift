class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var numIndices = [Int: Int]()  // Dictionary to store indices of numbers
        
        for (i, num) in nums.enumerated() {
            let complement = target - num
            if let complementIndex = numIndices[complement] {
                return [complementIndex, i]
            }
            numIndices[num] = i
        }
        
        // Since the problem guarantees exactly one solution, we don't need to return an empty array.
        // We add this line to satisfy the return type, but it should never be reached.
        return []
    }
}
