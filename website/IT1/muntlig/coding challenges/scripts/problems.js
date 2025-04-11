const descriptionEl = document.getElementById("description");
const codeEl = document.getElementById("code");
const consoleEl = document.getElementById("console");
const dividerDescCodeEL = document.getElementById("divider_desc_code");
const dividerCodeConsEl = document.getElementById("divider_code_cons");
const containerEl = document.getElementsByClassName("flexlayout")[0];

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

class Divider {
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

function resize() {
    for (const i of [codeEl, dividerCodeConsEl, consoleEl]) {
        i.style["width"] = `${containerEl.clientWidth - parseInt(i.style["left"])}px`;
    }
    for (const i of [descriptionEl, dividerDescCodeEL, consoleEl]) {
        i.style["height"] = `${containerEl.clientHeight - parseInt(i.style["top"])}px`;
    }
}

const dividers = [
    new Divider(dividerDescCodeEL, [descriptionEl], [codeEl, dividerCodeConsEl, consoleEl]),
    new Divider(dividerCodeConsEl, [codeEl], [consoleEl])
];

addEventListener("resize", resize.bind(this));
resize();


var editor = ace.edit("editor");
editor.setTheme("ace/theme/monokai");
editor.session.setMode("ace/mode/javascript");

function saveCode() {
    if (!confirm("Do you want to save your code?\nThis will overwrite your previously saved code.")) return;
    const code = editor.getValue();
    localStorage.setItem('user-code', code);
}
function loadCode(skip=false) {
    if (!(skip || confirm("Do you want to load your last saved code?\nYour current code will be deleted."))) return;
    const code = localStorage.getItem('user-code') || '';
    editor.setValue(code);
}

localStorage.getItem("user-code") ? loadCode(true) : resetCode();