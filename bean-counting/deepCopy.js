const data1 = {
    obj: {
        key: 'Key',
    },
}

function deepCopy(obj) {
    const keys = Object.keys(obj)

    const newObject = {}

    for (let i = 0; i < keys.length; i++) {
        const key = keys[i]
        if (typeof obj[keys[i]] === 'object') {
            newObject[key] = deepCopy(obj[key])
        } else {
            newObject[key] = obj[key]
        }
    }

    return newObject
}

const data = deepCopy(data1)

if (data1.obj.key === data.obj.key) {
    console.log("true");
} else {
    console.log("false");
}