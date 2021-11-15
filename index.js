const inputArea = document.querySelector("#input_text_area")
const outputArea = document.querySelector("#output_text_area")
const complexity = document.querySelector("#complexity")

const obfuscate = (finalTaskSolution) => {
	console.log("works");
    const bytes = utf8.encode(finalTaskSolution);
    finalTaskSolution = base64.encode(bytes);
    const array = finalTaskSolution.match(/.{1,50}/g);
    let pythonString = '';
    for (let i = 0; i < array.length; i++) {
        if (!(i == 0)) {
            pythonString += "         ";
        }
        pythonString += `b'${array[i]} '`
        if (!(i == array.length - 1)) {
            pythonString += "\\\n"
        }
    }
    console.log(pythonString);
    return `
from base64 import b64encode, b64decode
hidden = ${pythonString}
eval(compile(b64decode(hidden.decode()), "<string>", "exec"))
    `;
}

function isNumeric(value) {
    return /^-?\d+$/.test(value);
}

const update = () => {

	if (inputArea.value == "") {
		outputArea.value = ""
		return
	}

	obfuscated = obfuscate(inputArea.value)

    if (isNumeric(complexity.value)) {
        for (let i = 1; i < parseInt(complexity.value); i++) {
            obfuscated = obfuscate(obfuscated)
        }
    }

    outputArea.value = obfuscated
}

inputArea.addEventListener("input", () => {
    update()
})

complexity.addEventListener("input", () => {
    update()
})