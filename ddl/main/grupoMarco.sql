create table grupoMarco
(
    NAME text
        constraint PK_grupoMarco
            primary key,
    TYPE text,
    constraint CH_grupoMarco_type
        check (TYPE IN ('C', 'U'))
);

