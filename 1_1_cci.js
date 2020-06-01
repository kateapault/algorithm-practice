// "IsUnique"
// take a string, check to see if all letters are unique in the string
// return true if there are no repeats, otherwise return false

// 'asdfghjkl' => true
// 'aabb' => false

// iterate through string
// put each letter into object or set -> exit out of iteration 
// as soon as there's duplicate
// if not, return true

function is_unique(string) {
    let characters = new Set()
    for (let i=0;i<string.length;i++) {
        let char = string[i]
        if (characters.has(char)) {
            return false
        } else {
            characters.add(char)
        }
    }
    return true
}

console.log('string: "abcd" expected output: true')
console.log(is_unique('abcd'))
console.log('string: "abcc" expected output: false')
console.log(is_unique('abcc'))