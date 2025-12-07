create table grupoVidrio
(
    NAME text
        constraint PK_grupoVidrio
            primary key,
    TYPE text,
    constraint CH_grupoVidiro_type
        check (TYPE IN ('C', 'U'))
);

