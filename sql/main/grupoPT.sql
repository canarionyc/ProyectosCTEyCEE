create table grupoPT
(
    NAME VARCHAR2(100)
        constraint PK_grupoPT
            primary key,
    TYPE VARCHAR2(1),
    constraint CH_grupoPT_type
        check (TYPE IN ('C', 'U'))
);

