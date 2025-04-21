# le da porta serial e escreve em arquivo
# Uso:
# python ler_porta_serial.py arquivo_saida.txt

# importa biblioteca para ler da porta serial
import serial

import sys

# qual porta serial?
serial_port = 'COM9'

# qual taxa? (ajustada no codigo do Arduino na linha "Serial.begin(minha_taxa)")
baud_rate = 9600;

# onde escrever resultado?
write_to_file_path = sys.argv[1]

# abre arquivo, apagando conteudo anterior
output_file = open(write_to_file_path, "w+")

# abre porta serial
ser = serial.Serial(serial_port, baud_rate)

# para sempre:
while True:
    # le da entrada serial
    line = ser.readline()

    # transforma em UTF-8, caso o que tenha sido lido, tenha sido lido em binario
    line = line.decode("utf-8").strip()
    #if len(line) == 0:
    #    continue

    # mostra na tela
    print(line)

    # escreve no arquivo
    output_file.write(line+"\n")