---
title: Desenvolvimento do Frontend
sidebar_position: 1
description : Frontend desenvolvido na sprint 3
---

# Documentação do Projeto
# Introdução

Nesta sprint 3, o grupo Käfer começou a construir o frontend proposto para uso da solução. Tendo o mockup, desenvolvido na sprint anterior, como base, a aplicação foi desenvolvida utilizando Typescript com Vite e Tailwind, tecnologias que serão explicadas melhor no próximo tópico desta documentação. Ademais, conceitos de UX foram aplicados durante a construção do frontend de modo que a interface fosse feita da melhor forma possível para o usuário final. Dessa forma, criamos telas para a aplicação web deste projeto, que pode ser observado nesta documentação e na pasta frontend do nosso repositório

## Tecnologias Utilizadas
**TypeScript** é uma linguagem de programação que estende o JavaScript, adicionando tipos estáticos. Ao utilizar `.tsx`, estamos lidando com arquivos que combinam TypeScript e JSX, permitindo a criação de componentes React com a segurança adicional de tipos, o que torna o desenvolvimento mais robusto e fácil de manter. O TypeScript ajuda a detectar erros durante o desenvolvimento, evitando problemas em tempo de execução.

### Vite
**Vite** é uma ferramenta de build que oferece um ambiente de desenvolvimento rápido e otimizado. Diferentemente de ferramentas como Webpack, o Vite carrega os módulos sob demanda, resultando em um tempo de inicialização quase instantâneo, especialmente útil em projetos React. Ele também permite uma integração eficiente com TypeScript e frameworks como Tailwind.

### Tailwind CSS
**Tailwind CSS** é um framework CSS utilitário que permite a criação rápida de interfaces de usuário ao fornecer classes de estilos predefinidas. Ele possibilita a criação de layouts responsivos e bem estilizados sem a necessidade de escrever CSS personalizado, o que acelera o desenvolvimento e garante consistência.

## Estrutura do Código

### 1. **Home.tsx**

O componente `Home` é a página principal da aplicação. Ele utiliza o `useState` para gerenciar o estado de visibilidade do popup e `useNavigate` para controlar a navegação entre as páginas. Dois botões principais permitem ao usuário executar um modelo ou iniciar o processo de treinamento.

#### Partes Importantes:
- **Estado e navegação**: O `useNavigate` permite a navegação programática entre páginas. Por exemplo, o botão "Executar" redireciona para `/exc`, enquanto o botão "Treinar" abre um popup modal.
- **Popup Modal**: O modal é controlado por um estado booleano (`isPopupVisible`). A função `handleConfirm` fecha o modal e redireciona para a página de treinamento.

```typescript
*TypeScript* é uma linguagem de programação que estende o JavaScript, adicionando tipos estáticos. Ao utilizar .tsx, estamos lidando com arquivos que combinam TypeScript e JSX, permitindo a criação de componentes React com a segurança adicional de tipos, o que torna o desenvolvimento mais robusto e fácil de manter. O TypeScript ajuda a detectar erros durante o desenvolvimento, evitando problemas em tempo de execução.

### Vite
*Vite* é uma ferramenta de build que oferece um ambiente de desenvolvimento rápido e otimizado. Diferentemente de ferramentas como Webpack, o Vite carrega os módulos sob demanda, resultando em um tempo de inicialização quase instantâneo, especialmente útil em projetos React. Ele também permite uma integração eficiente com TypeScript e frameworks como Tailwind.

### Tailwind CSS
*Tailwind CSS* é um framework CSS utilitário que permite a criação rápida de interfaces de usuário ao fornecer classes de estilos predefinidas. Ele possibilita a criação de layouts responsivos e bem estilizados sem a necessidade de escrever CSS personalizado, o que acelera o desenvolvimento e garante consistência.

## Estrutura do Código

### 1. *Home.tsx*

O componente Home é a página principal da aplicação. Ele utiliza o useState para gerenciar o estado de visibilidade do popup e useNavigate para controlar a navegação entre as páginas. Dois botões principais permitem ao usuário executar um modelo ou iniciar o processo de treinamento.

<p align="center"><b> Figura 1 - Home</b></p>
<div align="center" class="zoom-image">
  <img src={require('../../../../static/img/home.png').default} alt="home"/>
  <p><b>Fonte:</b> Elaborado pelo grupo Käfer</p>
</div>

#### Partes Importantes:
- *Estado e navegação*: O useNavigate permite a navegação programática entre páginas. Por exemplo, o botão "Executar" redireciona para /exc, enquanto o botão "Treinar" abre um popup modal.
- *Popup Modal*: O modal é controlado por um estado booleano (isPopupVisible). A função handleConfirm fecha o modal e redireciona para a página de treinamento.

```

```typescript
const handleExecuteClick = () => {
    navigate('/exc');  
};

const handleTrainClick = () => {
    setIsPopupVisible(true); 
};
```

### 2. *ExcModelPage.tsx*

Esta página exibe o resultado de um modelo executado, incluindo gráficos e métricas. O uso de estados permite controlar a abertura de popups, e a estrutura de layout com Tailwind facilita a estilização da página.

<p align="center"><b> Figura 2 - ExcModelPage</b></p>
<div align="center" class="zoom-image">
  <img src={require('../../../../static/img/trainedModelPage.png').default} alt="ExcModelPage"/>
  <p><b>Fonte:</b> Elaborado pelo grupo Käfer</p>
</div>


#### Partes Importantes:
- *Seção de Resultados*: São exibidos o resultado atual e o modelo anterior, com caixas estilizadas utilizando Tailwind.
- *Gráficos Placeholder*: Espaços são reservados para gráficos e métricas, permitindo futura integração com bibliotecas de visualização.

```
<div className="w-full bg-gray-300 h-10 rounded-lg flex justify-center items-center">
  <span className="text-black">XXXXXX</span>
</div>
```

### 3. *ExcPage.tsx*

A página ExcPage lida com o upload de arquivos e a inserção de dados necessários para a execução de modelos. Inclui componentes reutilizáveis como FileUpload e KNRInput.

<p align="center"><b> Figura 3 - ExcPage</b></p>
<div align="center" class="zoom-image">
  <img src={require('../../../../static/img/trainingPage.png').default} alt="EcxPage"/>
  <p><b>Fonte:</b> Elaborado pelo grupo Käfer</p>
</div>


#### Partes Importantes:
- *Componente de Input*: Um campo de entrada é fornecido para que o usuário insira seu KNR. O botão "Confirmar" navega para a página de progresso da execução do modelo.
- *File Upload*: O componente FileUpload facilita o upload de arquivos, como .csv, necessários para a análise.

```
<KNRInput />
<ConfirmButton />
```

### 4. *ExcProgressPage.tsx*

Essa página simula o progresso da execução de um modelo, exibindo uma barra de progresso que é atualizada periodicamente usando useEffect.

<p align="center"><b> Figura 4 - ExcProgressPage</b></p>
<div align="center" class="zoom-image">
  <img src={require('../../../../static/img/trainingProgressPage.png').default} alt="ExcProgressPage"/>
  <p><b>Fonte:</b> Elaborado pelo grupo Käfer</p>
</div>


#### Partes Importantes:
- *Simulação de Progresso*: O estado progress é atualizado a cada segundo até atingir 100%, simulando a execução de um modelo de machine learning.
- *Barra de Progresso*: Um componente BarExc é responsável por renderizar visualmente o progresso.

```
useEffect(() => {
  const interval = setInterval(() => {
    setProgress((prev) => {
      if (prev < 100) {
        return prev + 10;
      } else {
        clearInterval(interval);
        return 100;
      }
    });
  }, 1000);
}, []);
```

### 5. **App.tsx**

O componente `App` é o ponto de entrada da aplicação, responsável por definir as rotas utilizando o `react-router-dom`. Cada rota mapeia um caminho específico para um componente.

#### Partes Importantes:
- **Rotas**: O sistema de rotas é responsável por controlar a navegação entre páginas. Por exemplo, a rota `/exc` leva à página `ExcPage`, enquanto `/excProgress` leva à página de progresso.

```typescript
<Routes>
  <Route path="/" element={<Home />} />
  <Route path="/exc" element={<ExcPage />} />
  <Route path="/excProgress" element={<ExcProgressPage />} />
</Routes>
```

### 6. *TrainingPage.tsx*

Ao clicar no botão treinar na tela inicial, a tela de treinamento é exibida, em que disponibiliza uma opção para inserir dados em formato de csv para treinar o modelo

<p align="center"><b> Figura 5 - TrainingPage</b></p>
<div align="center" class="zoom-image">
  <img src={require('../../../../static/img/trainingPage.png').default} alt="TrainingPage"/>
  <p><b>Fonte:</b> Elaborado pelo grupo Käfer</p>
</div>


Também, vale destacar alguns dos componentes que estão presentes na tela. Um deles é o Header, que é a parte superior da tela, em que o usuário consegue saber em que tela está, e consegue retornar para telas anteriores ao clicar no nome da tela anterior. O código a seguir ilustra um pouco o funcionamento do header:

```typescript
const Header: React.FC = () => {
  const location = useLocation();
  const currentPage = pageNames[location.pathname] || 'Página Desconhecida';

  return (
    <header className="flex items-center space-x-4 p-4">
      <Link to="/" className="text-gray-400 hover:text-white">Home</Link>
      <span className="text-gray-400">{'>'}</span>

      <span className="text-white">{currentPage}</span>
    </header>
  );
};
```

Um outro componente presente nesta tela é o File Upload, que permite o upload de arquivos csv. Segue um trecho do código deste componente:

```typescript
const FileUpload: React.FC = () => {
    return (
      <div className="font-sans flex flex-col items-center justify-center border-2 border-dashed bg-gradient-to-b from-[#333641] to-[#2D3039] h-64 w-full max-w-lg mx-auto mt-10 bg-gray-800 rounded-lg">
        <label className="cursor-pointer">
          <div className="flex flex-col items-center space-y-2">
            <svg width="150" height="150" viewBox="0 0 150 150" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect x="40" y="70" width="70" height="40" rx="5" stroke="#888888" stroke-width="6" />
            <circle cx="95" cy="90" r="4" fill="#888888" />
            <path d="M75 30 L75 80" stroke="#888888" stroke-width="6" stroke-linecap="round" />
            <path d="M60 45 L75 30 L90 45" stroke="#888888" stroke-width="6" stroke-linecap="round" />
            </svg>
            <p className="text-white">Adicione seu .csv para treinar o modelo</p>
          </div>
          <input type="file" accept=".csv" className="hidden" />
        </label>
      </div>
    );
  };
```

### 7. *TrainingProgressPage*

Esta tela apenas exibe o processo de treinamento do modelo, incluindo uma progress bar, que mostra o progresso do treinamento

<p align="center"><b> Figura 6 - TrainingProgressPage</b></p>
<div align="center" class="zoom-image">
  <img src={require('../../../../static/img/trainingProgressPage.png').default} alt="TrainingProgressPage"/>
  <p><b>Fonte:</b> Elaborado pelo grupo Käfer</p>
</div>

Para realizar o funcionamento desta progress bar, o componente dele foi devidamente criado e configurado, e pode ser exemplificado no seguinte trecho de código:

```typescript
const ProgressBar: React.FC<ProgressBarProps> = ({ progress }) => {
    const navigate = useNavigate();

    useEffect(() => {
        if (progress === 100) {
          navigate('/trained');
        }
      }, [progress, navigate]);
  return (
    <div className="w-full bg-gray-700 rounded-full h-2.5 mt-8">
      <div
        className="bg-blue-500 h-2.5 rounded-full"
        style={{ width: `${progress}%` }}
      />
    </div>
  );
};
```
### 8. *TrainedModelPage*

Exibe os resultados do treinamento do modelo, com a exibição de gráficos e métricas. Além disso, são exibidos, além dos resultados do modelo atual, os resultados do modelo antigo, o que torna possível fazer comparações entre modelos diferentes

<p align="center"><b> Figura 7 - TrainedModelPage</b></p>
<div align="center" class="zoom-image">
  <img src={require('../../../../static/img/trainedModelPage.png').default} alt="TrainedModelPage"/>
  <p><b>Fonte:</b> Elaborado pelo grupo Käfer</p>
</div>

Dada a exibição desses dois modelos, é possível escolher entre qual deles para prosseguir com a execução do modelo. Para isso ser possível, foi criado um componentes para a exibição de um pop up, que aparece quando um usuário clica no modelo atual ou no anterior, e exibe uma mensagem de confirmação para o uso de tal modelo:

```typescript
const ConfirmationPopup: React.FC<ConfirmationPopupProps> = ({ onClose }) => {
  const navigate = useNavigate();

  const handleConfirm = () => {
    // Redireciona para a tela de modelo treinado
    navigate('/tabela');
  };

  return (
    <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50">
      <div className="bg-gradient-to-b from-gray-800 to-gray-900 p-8 rounded-xl shadow-lg text-center">
        <h2 className="text-white text-xl mb-8">Tem certeza que deseja utilizar esse modelo?</h2>
        <div className="flex justify-around">
          <button
            className="bg-green-500 text-white px-4 py-2 rounded-md hover:bg-green-600"
            onClick={handleConfirm}
          >
            Sim
          </button>
          <button
            className="bg-red-500 text-white px-4 py-2 rounded-md hover:bg-red-600"
            onClick={onClose}
          >
            Não
          </button>
        </div>
      </div>
    </div>
  );
};
```
