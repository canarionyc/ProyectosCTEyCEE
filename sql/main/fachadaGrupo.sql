create table fachadaGrupo
(
    FACHADA VARCHAR2(100)
        constraint FK_fachadaGrupo2
            references tipoFachada,
    GRUPO   VARCHAR2(1)
        constraint FK_fachadaGrupo1
            references grupoPT,
    constraint PK_fachadaGrupo
        primary key (FACHADA, GRUPO)
);

