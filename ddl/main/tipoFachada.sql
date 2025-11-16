create table tipoFachada
(
    NAME VARCHAR2(100)
        constraint PK_tipoFachada
            primary key,
    TYPE VARCHAR2(1),
    constraint CH_PK_tipoFachada_type
        check (TYPE IN ('C', 'U'))
);

