create table grupo
(
    NAME  text
        constraint PK_grupo
            primary key,
    IMAGE text,
    TYPE  text,
    constraint CH_grupo_type
        check (TYPE IN ('C', 'U'))
);

