# Stake Arena - Projeto Online

## 🎯 Acesso à Aplicação

Seu projeto **Stake Arena Notificações** está online e acessível através do seguinte endereço:

**URL de Acesso:** https://5000-ij858jo4rocvzfhlcvp85-17d9fded.us2.manus.computer

---

## 📋 Informações do Projeto

### Arquitetura
- **Frontend**: React 19 + Vite + TailwindCSS + Socket.IO Client
- **Backend**: Flask + Flask-SocketIO + Python 3.11
- **Banco de Dados**: PostgreSQL (Neon Cloud)
- **Comunicação em Tempo Real**: Socket.IO

### Funcionalidades
- Sistema de autenticação de usuários
- Criação e gerenciamento de salas de apostas
- Sistema de apostas em tempo real
- Notificações via Socket.IO
- Rastreamento de usuários online
- Integração com WhatsApp

---

## 🗄️ Banco de Dados

O projeto está conectado ao banco de dados PostgreSQL no Neon Cloud com as seguintes configurações:

- **Host**: ep-aged-tooth-a5g5dkoi-pooler.us-east-2.aws.neon.tech
- **Database**: neondb
- **User**: neondb_owner
- **Port**: 5432

### Tabelas Criadas
1. **usuarios** - Gerenciamento de usuários, pontos e status online
2. **salas** - Salas de apostas criadas pelos usuários
3. **apostas** - Registro de apostas realizadas nas salas

---

## 🚀 Como o Projeto Está Rodando

O servidor Flask está rodando em modo de desenvolvimento com as seguintes características:

- **Porta**: 5000
- **Host**: 0.0.0.0 (todas as interfaces)
- **Debug Mode**: Ativado
- **CORS**: Habilitado para todas as origens
- **Socket.IO**: Ativo para comunicação em tempo real

### Arquivos Servidos
O backend está servindo os arquivos estáticos do frontend (build do React) através da pasta `/backend/static/`, permitindo que toda a aplicação seja acessada através de uma única URL.

---

## 📁 Estrutura do Projeto

```
projeto-stake-arena/
├── backend/
│   ├── main.py                 # Servidor Flask principal
│   ├── database_config.py      # Configuração do banco de dados
│   ├── socketio_instance.py    # Instância do Socket.IO
│   ├── routes/                 # Rotas da API
│   │   ├── auth.py            # Autenticação
│   │   ├── usuarios.py        # Gerenciamento de usuários
│   │   ├── salas.py           # Gerenciamento de salas
│   │   ├── apostas.py         # Sistema de apostas
│   │   └── online.py          # Usuários online
│   ├── models/                 # Modelos de dados
│   └── static/                 # Frontend buildado (dist/)
├── frontend-src/
│   ├── App.jsx                 # Componente principal
│   ├── components/             # Componentes React
│   ├── hooks/                  # Custom hooks
│   └── lib/                    # Utilitários
├── package.json                # Dependências do frontend
├── requirements.txt            # Dependências do backend
└── vite.config.js             # Configuração do Vite
```

---

## ⚠️ Observações Importantes

1. **Ambiente de Desenvolvimento**: O servidor está rodando em modo de desenvolvimento. Para produção, considere usar um servidor WSGI como Gunicorn ou uWSGI.

2. **Persistência**: O servidor está rodando no sandbox e permanecerá ativo enquanto a sessão estiver aberta. Para deploy permanente, considere usar plataformas como:
   - **Render** (recomendado para Flask)
   - **Railway**
   - **Heroku**
   - **DigitalOcean App Platform**

3. **Banco de Dados**: O banco de dados PostgreSQL no Neon Cloud já está configurado e as tabelas foram criadas automaticamente na inicialização.

4. **Socket.IO**: A comunicação em tempo real está funcionando através do Socket.IO, permitindo notificações instantâneas entre usuários.

---

## 🔧 Comandos Úteis

### Verificar Status do Servidor
```bash
netstat -tuln | grep 5000
```

### Ver Logs do Servidor
```bash
tail -f /tmp/flask.log
```

### Reiniciar o Servidor
```bash
pkill -f "python3.11 main.py"
cd /home/ubuntu/projeto-stake-arena/backend
nohup python3.11 main.py > /tmp/flask.log 2>&1 &
```

### Rebuild do Frontend
```bash
cd /home/ubuntu/projeto-stake-arena
pnpm run build
rm -rf backend/static
cp -r dist backend/static
```

---

## 📱 Testando a Aplicação

Acesse a URL fornecida e você poderá:

1. **Criar uma conta** ou fazer login
2. **Criar salas de apostas** com valores iniciais
3. **Participar de salas** criadas por outros usuários
4. **Fazer apostas** em tempo real
5. **Ver usuários online** através do sistema de rastreamento
6. **Receber notificações** instantâneas via Socket.IO

---

## 🎉 Projeto Pronto!

Seu projeto está online e funcionando! Acesse o link e comece a usar a aplicação.
