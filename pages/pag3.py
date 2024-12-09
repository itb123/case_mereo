import streamlit as st
def main():
        #texto com formatação
        st.markdown("<h1 style='text-align: center; color: black;'>Modelo de avaliação</h1>", unsafe_allow_html=True)
         #divisao da pagina em 2 duas linhas, sendo a primeira em 2 coluanas.
        col1,col2 = st.columns(2)
        with col1:
            #texto com formatação
            st.markdown(
                """
                <div style='text-align: justify; font-size: 16px;'> 
                Para avalição do sucesso será medido:<br><br>
                - Engajamento: Aumento no número de metas criadas diretamente pelos colaboradores;<br><br>
                - Tempo médio para criação de metas: Verificação da redução do tempo gasto na criação de metas;<br><br>
                - Quantidade de metas reprovadas ou editadas: Contabilização das metas reprovadas ou editadas pelos administradores.<br><br> 
                - Alinhamento estratégico: Medir a aderência (%) das metas aos objetivos estratégicos da corporação. <br><br>
                - Satisfação dos administradores e colaboradores: Medição da satisfação dos administradores em relação à automação do processo e dos colaboradores em relação ao sistema de recomendação, por meio de feedback qualitativo.
                  </div>
                """,unsafe_allow_html=True)

        with col2:
            st.image("img//engajamento.jpg",caption="Engajamento do time.")
            st.image("img//produtividade.jpg","Aumento de produtividade")
        #informações da barra lateral
        st.sidebar.header("Sobre")
        st.sidebar.markdown(
                        """
                        Selecione uma das páginas acima!

                        """
                            )
        
        
main()