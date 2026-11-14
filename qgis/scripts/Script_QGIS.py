
import os
import re
import sys
import time
from PyQt5.QtWidgets import QApplication, QFileDialog


# ============================================================
# 1. EXECUTION MODE
# ============================================================

# "normal" = execute scripts a1 to a22
# "reset"  = execute scripts a23 to a25

MODE = "normal"


# ============================================================
# 2. SELECT THE FOLDER CONTAINING THE SCRIPTS
# ============================================================

app = QApplication.instance()

if app is None:
    app = QApplication(sys.argv)

ruta_codigos = QFileDialog.getExistingDirectory(
    None,
    "Select the folder containing the QGIS scripts"
)

if not ruta_codigos:
    print("No folder selected. Execution cancelled.")
    sys.exit()


# ============================================================
# 3. FIND AND SORT THE SCRIPTS
# ============================================================

archivos = [
    archivo
    for archivo in os.listdir(ruta_codigos)
    if archivo.lower().endswith(".txt")
]

def numero_script(nombre):
    coincidencia = re.match(r'^a(\d+)', nombre, re.IGNORECASE)

    if coincidencia is None:
        raise ValueError(
            f"Unexpected script filename: {nombre}"
        )

    return int(coincidencia.group(1))


archivos = sorted(archivos, key=numero_script)


# ============================================================
# 4. VALIDATE THE SCRIPTS
# ============================================================

if len(archivos) != 25:
    raise ValueError(
        f"Expected 25 scripts, but found {len(archivos)}."
    )

numeros = [numero_script(archivo) for archivo in archivos]

if numeros != list(range(1, 26)):
    raise ValueError(
        "The scripts must be numbered consecutively from a1 to a25."
    )


# ============================================================
# 5. SELECT THE EXECUTION GROUP
# ============================================================

if MODE == "normal":

    scripts_ejecutar = archivos[:22]

elif MODE == "reset":

    scripts_ejecutar = archivos[22:25]

else:

    raise ValueError("Invalid execution mode.")


# ============================================================
# 6. EXECUTE THE SELECTED SCRIPTS
# ============================================================

tiempo_inicio = time.time()

print(f"Execution mode: {MODE}")
print(f"Number of scripts: {len(scripts_ejecutar)}")

for archivo in scripts_ejecutar:

    ruta_archivo = os.path.join(ruta_codigos, archivo)

    print(f"Executing {archivo}...")

    with open(ruta_archivo, "r", encoding="utf-8") as f:
        codigo = f.read()

    exec(codigo)

tiempo_total = time.time() - tiempo_inicio

print("Execution completed.")
print(f"Total execution time: {tiempo_total:.2f} seconds.")
