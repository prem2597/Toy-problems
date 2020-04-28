function countBs(_strings) {
    if (typeof _strings === 'string') {
        var count = 0
        for (let i = 0; i < _strings.length; i++) {
            if (_strings[i] === "B") {
                count ++;
            }
        }
        return count;
    }
}

console.log(countBs("Hello"));

function countChar(_strings, delta) {
    if (typeof _strings === 'string' && typeof delta === 'string') {
        var count = 0;
        for (let i = 0; i < _strings.length; i++) {
            if (_strings[i] === delta) {
                count ++;
            }
        }
        return count;
    }
}

console.log(countChar("hello","l"))