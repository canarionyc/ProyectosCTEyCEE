create table marco
(
    NAME         text
        constraint PK_marco
            primary key,
    GRUPO        text
        constraint FK_marco
            references grupoMarco,
    ABSORTIVIDAD NUMBER(5, 5),
    UMARCO       NUMBER(5, 5),
    TYPE         text,
    constraint CH_marco_type
        check (TYPE IN ('C', 'U'))
);

