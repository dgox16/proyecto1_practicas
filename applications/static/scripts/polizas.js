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

function colocarValores(numero, estado) {
	if (estado) {
		if (numero == 1) {
			tab1.style.display = "block";
		}
		if (numero == 2) {
			tab2.style.display = "block";
		}
		if (numero == 3) {
			tab3.style.display = "block";
		}
		if (numero == 4) {
			tab4.style.display = "block";
		}
		if (numero == 5) {
			tab5.style.display = "block";
		}
		document.getElementById("id__" + numero + "-cuenta").required = true;
		document.getElementById("id__" + numero + "-cargo").required = true;
		document.getElementById("id__" + numero + "-sucursal").required = true;
		document.getElementById("id__" + numero + "-abono").required = true;
		document.getElementById("id__" + numero + "-proveedor").required = true;
		document.getElementById("id__" + numero + "-concepto").required = true;
		document.getElementById("id__" + numero + "-iva").required = true;
	} else {
		if (numero == 1) {
			tab1.style.display = "none";
		}
		if (numero == 2) {
			tab2.style.display = "none";
		}
		if (numero == 3) {
			tab3.style.display = "none";
		}
		if (numero == 4) {
			tab4.style.display = "none";
		}
		if (numero == 5) {
			tab5.style.display = "none";
		}
		document.getElementById("id__" + numero + "-cuenta").required = false;
		document.getElementById("id__" + numero + "-cargo").required = false;
		document.getElementById("id__" + numero + "-sucursal").required = false;
		document.getElementById("id__" + numero + "-abono").required = false;
		document.getElementById("id__" + numero + "-proveedor").required = false;
		document.getElementById("id__" + numero + "-concepto").required = false;
		document.getElementById("id__" + numero + "-iva").required = false;
	}
}

function visualizacionTab() {
	if (contador === 0) {
		colocarValores(1, false);
		colocarValores(2, false);
		colocarValores(3, false);
		colocarValores(4, false);
		colocarValores(5, false);
	}

	if (contador === 1) {
		colocarValores(1, true);
		colocarValores(2, false);
		colocarValores(3, false);
		colocarValores(4, false);
		colocarValores(5, false);
	}

	if (contador === 2) {
		colocarValores(1, true);
		colocarValores(2, true);
		colocarValores(3, false);
		colocarValores(4, false);
		colocarValores(5, false);
	}
	if (contador === 3) {
		colocarValores(1, true);
		colocarValores(2, true);
		colocarValores(3, true);
		colocarValores(4, false);
		colocarValores(5, false);
	}
	if (contador === 4) {
		colocarValores(1, true);
		colocarValores(2, true);
		colocarValores(3, true);
		colocarValores(4, true);
		colocarValores(5, false);
	}
	if (contador === 5) {
		colocarValores(1, true);
		colocarValores(2, true);
		colocarValores(3, true);
		colocarValores(4, true);
		colocarValores(5, true);
	}
}

const tab1 = document.getElementById("tab1");
const tab2 = document.getElementById("tab2");
const tab3 = document.getElementById("tab3");
const tab4 = document.getElementById("tab4");
const tab5 = document.getElementById("tab5");
const btnMas = document.getElementById("btnMas");
const btnMenos = document.getElementById("btnMenos");
let contador = 0;

window.onload = visualizacionTab();

btnMas.addEventListener("click", () => {
	if (contador < 5) {
		contador++;
	}

	visualizacionTab();
});

btnMenos.addEventListener("click", () => {
	if (contador > 0) {
		contador--;
	}
	visualizacionTab();
});
