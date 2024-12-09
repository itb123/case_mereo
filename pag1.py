import streamlit as st
def main():
    #titulo do pagina
    st.markdown("<h1 style='text-align: center; color: black;'>Case Mereo<br> -<br>  Melhoria no módulo de Performace</h1>", unsafe_allow_html=True)
    #divisao da pagina em 2 duas linhas, sendo a primeira em 2 coluanas.
    col1,col2 = st.columns(2)
    #primeira coluna
    with col1:
        #texto com formatação
        st.markdown(
        """
        <div style='text-align: justify; font-size: 16px;'> 
        A avaliação de desempenho é uma ferramenta que ajuda no desenvolvimento da equipe. 
        A partir de métricas e critérios claros, esse método ajuda a entender se o colaborador cumpre o que é esperado, excede as expectativas ou tem pontos de melhoria. 
        Para realizá-la de forma eficaz, é fundamental alinhar as expectativas com os colaboradores no início do período considerado para a avaliação. 
        Isso envolve levar em conta as responsabilidades da função, as metas do setor, as características culturais da empresa e o potencial de cada indivíduo.  
        Além de medir a performance do time, a avaliação de desempenho deve ser orientada para o futuro. É muito comum observarmos problemas na avaliação de desempenho, muitas vezes por falta de adesão dos colaboradores ou uma má compreensão da proposta. 
        Pensando na experiência do usuário temos os principais problemas: 
        </div>
        """,unsafe_allow_html=True)
    #segunda coluna
    with col2:
        #upload de imagens
        st.image("img//clima-organizacional.jpg",caption=" Definição de metas/objetivos.")
        st.image("img//satisfacao-cliente.jpg",caption="Satisfação do usúario.")    
    #texto
    st.write(
       """

        - Reduzição da complexidade no processo: O preenchimento manual dos vários campos, com múltiplos critérios, tornando o processo demorado e sem orientações, resultando frustações 
        - Falta de alinhamento estratégico com a corporação, metas que não estão ligadas aos objetivos estratégicos da empresa resultando na diminuição da eficácia organizacional.
        - Metas que não consideram o histórico, cargo ou responsabilidades dos colaboradores resultando em metas genéricas ou irrelevantes.
        """
    )
    #texto com formatação  
    st.markdown("# Relevância do problema")
    st.markdown(
        """
        <div style='text-align: justify; font-size: 16px;'> 
            Os problemas são apenas alguns dos vários existentes durante o processo de avalição de desempenho. 
            Dentro as principais vantagens em resolver esses pontos, temos como destaque: Processo simples: Aumento da usabilidade do sistema pelos colaboradores e gestores. 
            Automatização das etapas de criação de metas e cadastro: Permite que colaboradores e gestores possam dedicar seu tempo em tarefas mais táticas. 
            Metas claras e objetivas: Garantem maior contribuição para a empresa gerando maiores lucros, expansão da área de negócios e benefícios para os colaboradores. 
            Impactando usuário final: Produto com elevado desempenho, gerando competitividade no mercado.
            Pensando nos problemas e nos possíveis ganhos, proponho a abordagem de: “Sistema de recomendação de metas personalizadas utilizando Inteligência Artificial e Automação de processos”.
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