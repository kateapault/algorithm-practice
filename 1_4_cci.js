// palindrome permutation
// given a string, check to see if it's a permutation of a 
// palindrome. cases and non-letter characters can be ignored 

// 'Tact coa' => true ('tacocat')
// 'asdfgh' => false

// go through string, count letters in object, as long as # of letters 
// that appear an odd number of times is < 2 (1 or 0), then it can be
// rearranged => true

function palindrome_permutation(string) {
    let odd_characters = {}
    for (let i=0;i<string.length;i++) {
        let char = string[i]
        if (char !== ' ' && odd_characters[char]) {
            delete odd_characters[char]
        } else if (char !== ' ' && !odd_characters[char]) {
            odd_characters[char] = 1
        }
    }
    if (Object.values(odd_characters).length <= 1) {
        return true
    }
    return false
}

console.log('string: "asdfgh", expected output: false ')
console.log(palindrome_permutation('asdfgh'))
console.log('string: "taco cat", expected output: true')
console.log(palindrome_permutation("taco cat"))