# AI Engeneering-Fiap2025

 https://arnaldojr.github.io/cognitivecomputing/
Para implementar os Thresholds de Alerta por Sensor no Node-RED, você precisa criar um fluxo que:

1. Receba os dados JSON (como esse do seu inject).


2. Avalie cada sensor de uma região com base nos thresholds fornecidos.


3. Monte um JSON de alerta, incluindo:

Sensores em nível Atenção, Alerta ou Crítico;

O pior nível encontrado (nivel_alerta_geral);

O timestamp e as coordenadas da região.



4. Publique o alerta no tópico MQTT defesa_civil/alertas/<seu_rm>.




---

✅ Etapas práticas no Node-RED

1. Função para classificar o nível de cada sensor

Crie um nó function chamado classificaNivel com algo assim:

// Define os thresholds por sensor
const thresholds = {
  nivel_rio:       [40, 60, 80],
  pluviometro:     [10, 30, 50],
  inclinometro:    [2, 10, 15],
  sismografo:      [2.0, 4.0, 6.0],
  umidade_solo:    [60, 70, 90],
  temperatura:     [35, 40, 45],
  detector_fumaca: [10, 60, 80],
  velocidade_vento:[20, 50, 80],
  barometro:       [980, 990, 1010, 1020],
  radar_doppler:   [30, 70, 90],
  acelerometro:    [0.2, 0.5, 0.8],
  magnetometro:    [50, 100, 150],
  umidade_ar:      [70, 80, 90],
  radar_chuva:     [20, 40, 60],
};

// Função para determinar o nível
function getNivel(sensor, valor) {
  const t = thresholds[sensor];
  if (!t) return 'desconhecido';

  if (sensor === 'barometro') {
    if (valor < t[0]) return 'crítico';
    if (valor < t[1]) return 'alerta';
    if (valor < t[2]) return 'atenção';
    if (valor <= t[3]) return 'normal';
    return 'atenção'; // Acima de 1020
  }

  if (valor <= t[0]) return 'normal';
  if (valor <= t[1]) return 'atenção';
  if (valor <= t[2]) return 'alerta';
  return 'crítico';
}

// Parâmetros fixos
const rm = "<seu_rm>";
const regiao = "sudeste"; // troque pela sua região

const dados = msg.payload.dados_por_regiao[regiao];
const sensores = dados.sensores;
const sensores_criticos = {};
let nivelGeral = 'normal';

const prioridade = ['normal', 'atenção', 'alerta', 'crítico'];

for (let sensor in sensores) {
  const valor = sensores[sensor];
  const nivel = getNivel(sensor, valor);

  if (nivel !== 'normal') {
    sensores_criticos[sensor] = valor;
    if (prioridade.indexOf(nivel) > prioridade.indexOf(nivelGeral)) {
      nivelGeral = nivel;
    }
  }
}

msg.payload = {
  aluno_rm: rm,
  regiao: regiao,
  coordenadas: dados.coordenadas,
  timestamp: msg.payload.timestamp,
  sensores_criticos: sensores_criticos,
  nivel_alerta_geral: nivelGeral
};

return msg;


---

2. Publicar no MQTT

Adicione um nó mqtt out, configure seu broker e publique no tópico:

defesa_civil/alertas/<seu_rm>


---

Se quiser, posso gerar esse fluxo completo em .json pra você importar direto no Node-RED. Deseja isso? Se sim, me informe seu RM e a região que está usando.

