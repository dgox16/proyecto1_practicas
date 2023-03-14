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

const colocarValores = (numero, estado) => {
    if (estado) {
        document.getElementById("poliza_detalle" + numero).style.display =
            "block";
        document.getElementById("id__" + numero + "-cuenta").required = true;
        document.getElementById("id__" + numero + "-cargo").required = true;
        document.getElementById("id__" + numero + "-sucursal").required = true;
        document.getElementById("id__" + numero + "-abono").required = true;
        document.getElementById("id__" + numero + "-proveedor").required = true;
        document.getElementById("id__" + numero + "-concepto").required = true;
        document.getElementById("id__" + numero + "-iva").required = true;
    } else {
        document.getElementById("poliza_detalle" + numero).style.display =
            "none";
        document.getElementById("id__" + numero + "-cuenta").required = false;
        document.getElementById("id__" + numero + "-cargo").required = false;
        document.getElementById("id__" + numero + "-sucursal").required = false;
        document.getElementById("id__" + numero + "-abono").required = false;
        document.getElementById(
            "id__" + numero + "-proveedor",
        ).required = false;
        document.getElementById("id__" + numero + "-concepto").required = false;
        document.getElementById("id__" + numero + "-iva").required = false;
    }
};

const visualizacionTab = (num) => {
    for (let index = 1; index <= num; index++) {
        if (index === contador) {
            for (let desdeInicio = 1; desdeInicio <= index; desdeInicio++) {
                colocarValores(desdeInicio, true);
            }
            for (
                let desdeContador = index + 1;
                desdeContador <= num;
                desdeContador++
            ) {
                colocarValores(desdeContador, false);
            }
        }
    }
};

const btnMas = document.getElementById("btnMas");
const btnMenos = document.getElementById("btnMenos");
const numDetalles = document.querySelectorAll("[id^=poliza_detalle]").length;
let contador = 1;

window.onload = visualizacionTab(numDetalles);

btnMas.addEventListener("click", () => {
    if (contador < numDetalles) {
        contador++;
        visualizacionTab(numDetalles);
    }
});

btnMenos.addEventListener("click", () => {
    if (contador > 1) {
        contador--;
        visualizacionTab(numDetalles);
    }
});
