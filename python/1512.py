class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        s = 0
        for i in range(len(nums)):
            n = nums[i:].count(nums[i])
            m = nums[:i].count(nums[i])
            s += int((n * (n - 1)) / 2)
            s -= int((m * (m - 1)) / 2)
        return s
# bunda shunday qonuniyat borki son n marta qatnashsa n*(n-1)/2 ta masala shartini qanoatlantiruvchi
# holat mavjud, shuning uchun bunday holatlarni o'zgaruvchiga qo'shib boramiz, lekin degan joyi ham bor
# masalan nums=[1,2,3,1,1,3] bo'lsa unda qatnashgan 1 lar soni 3 ta va 3*(3-1)/2->3 ta holat mavjud,
# va masalani shartida aytilganki elementlar indeksi o'zining indeksidandan kichik bo'lmasligi kerak, yani 3-indeksda
# turgan 1 uchun 1 ta holat mavjud(nums[3],nums[4]), lekin biz uni allaqachon sanaganmiz 1-safar 1 soni uchragan vaqtda
# shuning uchun hisoblagichdan bi qiymatni ayirib qo'yamiz

