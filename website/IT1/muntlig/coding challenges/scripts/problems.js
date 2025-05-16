const descriptionEl = document.getElementById("description");
const codeEl = document.getElementById("code");
const consoleEl = document.getElementById("console");
const dividerDescCodeEL = document.getElementById("divider_desc_code");
const dividerCodeConsEl = document.getElementById("divider_code_cons");
const containerEl = descriptionEl.parentElement;

//#region style
descriptionEl.style["left"] = "0px";
descriptionEl.style["top"] = "0px";
descriptionEl.style["width"] = `${Math.floor(containerEl.clientWidth * 0.5 - 4)}px`;
descriptionEl.style["height"] = `${Math.floor(containerEl.clientHeight)}px`;
codeEl.style["left"] = `${Math.floor(containerEl.clientWidth * 0.5 + 4)}px`;
codeEl.style["top"] = "0px";
codeEl.style["height"] = `${Math.floor(containerEl.clientHeight * 0.6 - 4)}px`;
codeEl.style["right"] = "0px"
consoleEl.style["left"] = `${Math.floor(containerEl.clientWidth * 0.5 + 4)}px`;
consoleEl.style["top"] = `${Math.floor(containerEl.clientHeight * 0.6 + 4)}px`;
consoleEl.style["bottom"] = "0px"
consoleEl.style["right"] = "0px"
dividerDescCodeEL.style["left"] = `${Math.floor(containerEl.clientWidth * 0.5 - 4)}px`;
dividerDescCodeEL.style["top"] = "0px";
dividerDescCodeEL.style["height"] = `${Math.floor(containerEl.clientHeight)}px`;
dividerCodeConsEl.style["left"] = `${Math.floor(containerEl.clientWidth * 0.5 + 4)}px`;
dividerCodeConsEl.style["top"] = `${Math.floor(containerEl.clientHeight * 0.6 - 4)}px`;
dividerCodeConsEl.style["right"] = `0px`
//#endregion

//#region dividers
class _Divider {
    constructor(divider, left, rigth) {
        this.divider = divider;
        this.isVertical = divider.classList.contains("flexlayout_divider_vert");
        this.left = left;
        this.rigth = rigth;
        this.isDragging = false;

        this.divider.addEventListener("mousedown", this.startDragging.bind(this));
    }

    startDragging(e) {
        this.isDragging = true;
        document.addEventListener('mousemove', this.dragging.bind(this));
        document.addEventListener('mouseup', this.stopDragging.bind(this));

        this.offset   = this.isVertical ? parseInt(this.divider.style["left"]) - e.clientX : parseInt(this.divider.style["top"]) - e.clientY;
        this.startPos = this.isVertical ? e.clientX : e.clientY;
        this.startLeft  = this.left .map(i => ({side: 0, left: parseInt(i.style["left"]), top: parseInt(i.style["top"]), width: parseInt(i.style["width"]), height: parseInt(i.style["height"]), minWidth: parseInt(i.style["min-width"]), minHeight: parseInt(i.style["min-height"])}));
        this.startRigth = this.rigth.map(i => ({side: 1, left: parseInt(i.style["left"]), top: parseInt(i.style["top"]), width: parseInt(i.style["width"]), height: parseInt(i.style["height"]), minWidth: parseInt(i.style["min-width"]), minHeight: parseInt(i.style["min-height"])}));
    }

    dragging(e) {
        if (!this.isDragging) return;
        let currentPos = this.isVertical ? e.clientX : e.clientY;
        let delta = this.startPos - currentPos;

        if (this.isVertical) {
            this.startLeft.concat(this.startRigth).forEach(i => {
                if ((i.side ? i.width + delta : i.width - delta) < 200) {
                    delta = (delta >=0 ? Math.min : Math.max)(delta, i.side ? 200 - i.width : i.width - 200);
                }
            });
            this.divider.style["left"] = `${this.startPos - delta + this.offset}px`;
            this.left.forEach((e, i) => {
                e.style["width"] = `${this.startLeft[i].width - delta}px`
            });
            this.rigth.forEach((e, i) => {
                e.style["left"] = `${this.startRigth[i].left - delta}px`
                e.style["width"] = `${this.startRigth[i].width + delta}px`
            });
        } else {
            this.startLeft.concat(this.startRigth).forEach(i => {
                if ((i.side ? i.height + delta : i.height - delta) < 200) {
                    delta = (delta >=0 ? Math.min : Math.max)(delta, i.side ? 200 - i.height : i.height - 200);
                }
            });
            this.divider.style["top"] = `${this.startPos - delta + this.offset}px`;
            this.left.forEach((e, i) => {
                e.style["height"] = `${this.startLeft[i].height - delta}px`
            });
            this.rigth.forEach((e, i) => {
                e.style["top"] = `${this.startRigth[i].top - delta}px`
                e.style["height"] = `${this.startRigth[i].height + delta}px`
            });
        }
    }

    stopDragging() {
        this.isDragging = false;
        document.removeEventListener('mousemove', this.dragging.bind(this));
        document.removeEventListener('mouseup', this.stopDragging.bind(this));
    }
}

function _resize() {
    for (const i of [codeEl, dividerCodeConsEl, consoleEl]) {
        i.style["width"] = `${containerEl.clientWidth - parseInt(i.style["left"])}px`;
    }
    for (const i of [descriptionEl, dividerDescCodeEL, consoleEl]) {
        i.style["height"] = `${containerEl.clientHeight - parseInt(i.style["top"])}px`;
    }
}

const _dividers = [
    new _Divider(dividerDescCodeEL, [descriptionEl], [codeEl, dividerCodeConsEl, consoleEl]),
    new _Divider(dividerCodeConsEl, [codeEl], [consoleEl])
];

addEventListener("resize", _resize.bind(this));
_resize();
//#endregion

//#region code execution
var editor = ace.edit("editor");
editor.setTheme("ace/theme/monokai");
editor.session.setMode("ace/mode/javascript");

const terminalEl = document.getElementById("terminal");
const terminalOutputEl = document.getElementById('output');
const commandInputEl = document.getElementById('command-input');
let commandHistory = [];
let historyIndex = -1;

const _catchConsoleLog = function() {
    const _originalConsoleLog = console.log;
    console.log = (...args) => {
        const message = args.map(arg => typeof arg === 'object' ? JSON.stringify(arg) : arg).join(' ');
        _appendToTerminal(message);
        _originalConsoleLog(...args);
    };
}
_catchConsoleLog();

commandInputEl.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
        const command = commandInputEl.value.trim();
        if (command) {
            _executeCommand(command);
            commandHistory.push(command);
            historyIndex = commandHistory.length;
            commandInputEl.value = '';
        }
    } else if (e.key === 'ArrowUp') {
        if (historyIndex > 0) {
            historyIndex--;
            commandInputEl.value = commandHistory[historyIndex];
        }
    } else if (e.key === 'ArrowDown') {
        if (historyIndex < commandHistory.length - 1) {
            historyIndex++;
            commandInputEl.value = commandHistory[historyIndex];
        }
    }
});

document.getElementById("terminal").addEventListener("click", function() {
    document.getElementById("command-input").focus();
});

const _appendToTerminal = function(text) {
    const line = document.createElement('div');
    line.textContent = text;
    terminalOutputEl.appendChild(line);
    terminalEl.scrollTo(0, terminalEl.scrollHeight);
}

const _executeCommand = function(command) {
    _appendToTerminal(`$ ${command}`);
    try {
        switch (command) {
            case "clear": {
                terminalOutputEl.innerHTML = '';
                return;
            }
            case "run": {
                _runCode()
                return;
            }
            case "load": {
                _loadCode()
                return;
            }
            case "save": {
                _saveCode()
                return;
            }
            case "reset": {
                _resetCode();
                return;
            }
            default: {
                const result = command.split(";").map(cmd => new Function(`return ${cmd}`)());
                result.forEach(r => console.log(r !== undefined ? r : 'Command executed'));
            }
        }
    } catch (error) {
        _appendToTerminal(`Error: ${error.message}`);
    }
}

const _saveCode = function() {
    if (!confirm("Do you want to save your code?\nThis will overwrite your previously saved code.")) return;
    const code = editor.getValue();
    localStorage.setItem(`user-code-${_funcName}`, code);
    console.log("Saved code");
}
const _loadCode = function(skip=false) {
    if (!(skip || confirm("Do you want to load your last saved code?\nYour current code will be deleted."))) return;
    const code = localStorage.getItem(`user-code-${_funcName}`) || '';
    editor.setValue(code);
    console.log("Loaded code");
}

const _resetCode = function(skip=false){
    if (!(skip || confirm("Do you want to reset the code?\nYour current code will be deleted."))) return;
    editor.setValue(_originalCode);
    console.log("Reset code")
}

const _doTests = function(func, tests) {
    try{
        let passes = 0;
        for (let i=0;i<tests.length;i++) {
            passes += _compare(tests[i][0], func(...tests[i].slice(1))) ? 1 : 0;
        };
        console.log(`Tests passed ${passes}/${tests.length}`);
    } catch (e) {
        console.log(`Error: ${e}`)
    }
}

const _runCode = function() {
    console.log('Running editor code...');
    const code = editor.getValue();
    const func = new Function(`${code.replace(/(?<!\\)\`/, "\`")}; return ${_funcName};`)();
    _doTests(func, _tests);
}

localStorage.getItem(`user-code-${_funcName}`) ? _loadCode(true) : _resetCode(true);
//#endregion