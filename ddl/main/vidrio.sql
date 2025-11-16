create table vidrio
(
    NAME        text
        constraint PK_vidiro
            primary key,
    GRUPO       text
        constraint FK_vidiro
            references grupoVidrio,
    FACTORSOLAR NUMBER(5, 5),
    UVIDRIO     NUMBER(5, 5),
    TYPE        text,
    constraint CH_vidiro_type
        check (TYPE IN ('C', 'U'))
);

