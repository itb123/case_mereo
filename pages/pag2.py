import streamlit as st
def main():
    #texto com formatação
    st.markdown("<h1 style='text-align: center; color: black;'>Prospota de solução</h1>", unsafe_allow_html=True)
    #divisao da pagina em 2 duas linhas, sendo a primeira em 2 coluanas.
    col1, col2= st.columns(2)
    #primeira coluna
    with col1:
        #texto com formatação 
        st.markdown(
        """<div style='text-align: justify; font-size: 16px;'> 
        Sistema de recomendação de metas personalizadas utilizando Inteligência Artificial e Automação de processos. 
        O modelo de recomendação terá como base um algoritmo de recomendação utilizando processamento de linguagem natural e embeddings para sugestão de metas, treinado com base nas metas e objetivos da empresa, histórico das metas e dados de desempenho dos anos anteriores. <br><br>
        Com isso o modelo vai gerar templates de metas personalizados, mesclando o objetivo do cargo do cargo do colaborador com o objetivo da empresa. Cabendo ao colaborador a decisão final a escolha da meta. A plataforma avaliará a meta escolhida e realizará uma análise semântica entre cada meta proposta e cada meta da empresa, gerando uma nota entra 0 e 1. Quanto mais próximo de 1, mais alinhado estará com objeto organizacional e quando mais próximo de 0, menos alinhado será.<br><br>
        Para os administradores/gestores, haverá um fluxo automatizado de aprovações de metas, com notificações. Contará também, com um card de metas e um dashboard que permite a acompanhamento das metas, evolução mês a mês e acumulado ao longo do ano.
        </div>
        """,unsafe_allow_html=True)
                    
    #texto com formatação
    st.markdown("<h1 style='text-align: center; color: black;'>Metodologia de desenvolvimento</h1>", unsafe_allow_html=True)
    #segunda coluna
    with col2:
        st.image("img//nlp.webp",caption="Processamento de Linguagem Natural - PLN")
        st.image("img//gif_embeggins.webp",caption="Aprendizado por embeddings")
    #texto com formatação
    st.markdown(
            """
            <div style='text-align: justify; font-size: 16px;'> 
                Inicialmente, será feito o levantamento de requisitos junto aos colaboradores e gestores para entender os critérios utilizados na avaliação das metas, quais os principais gargalos atuais e realizar um levantamento histórico de metas e resultados.
                A recomendação ocorrerá com base em processamento de linguagem Natural, utilizando o modelo pre-treinado SENTENCE-BERT (SBERT) é um modelo para geração de embeddings de sentenças, que são representações vetoriais de sentenças, o objeto do modelo é medir a similaridade entre as sentenças e recuperação de informações. 
                O modelo funciona com 3 etapas: 

            </div>
            """,unsafe_allow_html=True)            
    #texto
    st.write(
            """
            - Fine-Tuning (ajuste fino): o modelo é treinado para maximizar a similaridade entre sentenças semelhante e minimizar a similaridade entre sentenças não-semelhantes. 
            - Rede Siamês: é uma rede neural dentro do modelo que contém duas ou mais redes neurais idênticas, mas com estímulos (entradas) diferentes, para comparar pares de sentenças.
            - Triplet loss: são utilizados três exemplos de dados: uma âncora, uma positiva e uma negativa. A âncora é embeddings de referencia, a positiva é embeddings similar à âncora e a negativa é um embeddings diferente. 
            O objetivo é minimizar a distância entre a âncora e a positiva, ao mesmo tempo em que se maximizar a distância entre a âncora e a negativa.
            """
            )
    #texto com formatação
    st.markdown(
            """
            <div style='text-align: justify; font-size: 16px;'>
                A escolhe do modelo se deu pela eficiência na geração de embeddings, criando embeddings de alta qualidade que conseguem captaruar melhor o significado semântico das sentenças, além de sua escalabilidade, permitindo operações de similaridade muito rápidas.
                Após ingestão pelo modelo, são gerados os templates de metas ajustáveis pelos colaboradores, com base no aprendizado do modelo utilizando dados históricos de metas e desempenhos.
                Em seguida é feita a análise de similaridade meta e objetivo pelo modelo de inteligência artificial medindo o grau de aproximação do objetivo da empresa, variando entre 0 e 1. 
                Após a criação das metas, o sistema vai encaminhar uma notificação para a tela do gestor e aguarda sua aprovação para inserir no card metas. 
                Caso a meta seja reprovada o gestor/administrador tem a opção de devolver a meta ou editar-lá. A aprovação seguirá a hierarquia definida. 
                Após a aprovação dos gestores, o card de metas será atualizado fornecendo uma visão gerencial com alinhamento das metas individuais às estratégias da empresa e o status do progresso das metas.
            </div>
            """,unsafe_allow_html=True)  
    #informações da barra lateral
    st.sidebar.header("Sobre")
    st.sidebar.markdown(
                        """
                        Selecione uma das páginas acima!

                        """
            )
   
main()