const el = document.getElementById("id_tipo");
const box = document.getElementById("poliza_egreso");
el.addEventListener("change", function handleChange(event) {
    if (event.target.value === "E") {
        box.style.display = "block";
        document.getElementById("id_beneficiario").required = true;
        document.getElementById("id_banco").required = true;
        document.getElementById("id_cheque").required = true;
    } else {
        box.style.display = "none";
        document.getElementById("id_beneficiario").required = false;
        document.getElementById("id_banco").required = false;
        document.getElementById("id_cheque").required = false;
    }
});

const targetDiv = document.getElementById("tabp");
const btn = document.getElementById("toggle");
document.getElementById("id__1-cuenta").required = false;
document.getElementById("id__1-cargo").required = false;
document.getElementById("id__1-sucursal").required = false;
document.getElementById("id__1-abono").required = false;
document.getElementById("id__1-proveedor").required = false;
document.getElementById("id__1-concepto").required = false;
document.getElementById("id__1-iva").required = false;

btn.addEventListener("click", () => {
    if (targetDiv.style.display !== "none") {
        targetDiv.style.display = "none";
        document.getElementById("id__1-cuenta").required = false;
        document.getElementById("id__1-cargo").required = false;
        document.getElementById("id__1-sucursal").required = false;
        document.getElementById("id__1-abono").required = false;
        document.getElementById("id__1-proveedor").required = false;
        document.getElementById("id__1-concepto").required = false;
        document.getElementById("id__1-iva").required = false;
    } else {
        targetDiv.style.display = "block";
        document.getElementById("id__1-cuenta").required = true;
        document.getElementById("id__1-cargo").required = true;
        document.getElementById("id__1-sucursal").required = true;
        document.getElementById("id__1-abono").required = true;
        document.getElementById("id__1-proveedor").required = true;
        document.getElementById("id__1-concepto").required = true;
        document.getElementById("id__1-iva").required = true;
    }
});
