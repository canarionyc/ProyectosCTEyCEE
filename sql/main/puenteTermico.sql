create table puenteTermico
(
    NAME    VARCHAR2(100),
    FACHADA VARCHAR2(100)
        constraint FK_puenteTermico2
            references tipoFachada,
    FI      NUMBER(5, 5),
    IMAGE   VARCHAR2(200),
    TYPE    VARCHAR2(1),
    GRUPO   VARCHAR2(100)
        constraint FK_puenteTermico1
            references grupoPT,
    constraint PK_puenteTermico
        primary key (NAME, FACHADA, GRUPO),
    constraint CH_puenteTermico_type
        check (TYPE IN ('C', 'U'))
);

