# Relatório — Sistema de Comunicação Digital (BPSK / QPSK) com AWGN

## Resumo
Implementamos um sistema de comunicação digital completo: geração de dados (ASCII), codificação Manchester, modulações BPSK e QPSK, canal AWGN com controle de SNR, demodulação e cálculo de BER. Geramos gráficos comparativos BER vs SNR.

## Implementação
- **Geração de dados:** `utils.string_to_binary()`
- **Codificação:** `codificacao.manchester_encode()`
- **Modulação:** `modulacao.bpsk_modulate()` e `modulacao.qpsk_modulate()`
- **Canal AWGN:** `ruido.add_awgn_noise()` (suporta sinais complexos)
- **Demodulação:** `demodulacao.bpsk_demodulate()` e `demodulacao.qpsk_demodulate()`
- **Métrica:** `demodulacao.calculate_ber()`
- **Gráficos:** `graficos.plot_ber_vs_snr()`

## Observações técnicas
- QPSK foi implementada conforme o mapa fornecido:
  - 00 → +1 + j
  - 01 → -1 + j
  - 10 → +1 - j
  - 11 → -1 - j
- AWGN para sinais complexos é gerado com ruído gaussiano independente em I e Q com variância `noise_power/2`.
- Para comparação justa, usamos a **mesma energia por símbolo** para ambas modulações.

## Resultados
- O script `main.py` imprime BER instantâneo para SNR exemplo (10 dB) e gera o gráfico **BER vs SNR** comparando BPSK e QPSK.
- Em teoria, BER por bit de QPSK = BER de BPSK sob AWGN ideal (quando SNR é referenciado por energia por bit), porém nosso sistema aplica Manchester antes da modulação o que altera o espaçamento temporal — o comportamento observável nos resultados é consistente com expectativas.

## Conclusões
- QPSK permite **dobrar a taxa de transmissão** (2 bits/símbolo) mantendo desempenho por bit semelhante ao BPSK.
- Codificação Manchester melhora sincronismo mas aumenta largura de banda (duplica símbolos).
- Aumentar SNR reduz BER de forma exponencial na região de interesse.

## Como executar
```bash
python main.py
