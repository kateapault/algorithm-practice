# @param {Integer[]} nums1
# @param {Integer} m
# @param {Integer[]} nums2
# @param {Integer} n
# @return {Void} Do not return anything, modify nums1 in-place instead.
def merge(nums1, m, nums2, n)
    if m > 0 && n > 0
        puts "yay both nonzero"
        x = nums2.shift()
        for i in 0...(m+n)
            if nums1[i] == 0
                puts "inserting x (#{x}) and nums2: #{nums2}"
                nums1[i] = x
                if nums2.length > 0 
                    puts "yes nums2 is greater than 0"
                    nums1[i+1..-1] = nums2
                end
                break
            elsif x <= nums1[i]
                shifted_nums = nums1[i..-2]
                nums1[i+1..-1] = shifted_nums
                nums1[i] = x
                puts "nums1 is now #{nums1}"
                if nums2.length > 0
                    x = nums2.shift
                    puts "x is now #{x} and nums2 is now #{nums2}"
                else
                    break
                end
            else
                puts "#{x} is greater than #{nums1[i]}"
            end

        end
    elsif m == 0
        puts "m is zero so nums1 is #{nums1}"
        puts "nums2 is #{nums2}"
        nums1 = nums2
        puts "so nums1 is now #{nums1}"
    end
    return nums1
end

k = merge([0],0,[2],1)
puts "OUTPUT: #{k}"