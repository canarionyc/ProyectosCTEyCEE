create table main.cerramiento
(
    NAME          text
        constraint PK_cerramiento
            primary key,
    TRANS_TERMICA NUMBER(5, 5),
    PESOM2        NUMBER(5, 5)
);

create table main.grupo
(
    NAME  text
        constraint PK_grupo
            primary key,
    IMAGE text,
    TYPE  text,
    constraint CH_grupo_type
        check (TYPE IN ('C', 'U'))
);

create table main.grupoMarco
(
    NAME text
        constraint PK_grupoMarco
            primary key,
    TYPE text,
    constraint CH_grupoMarco_type
        check (TYPE IN ('C', 'U'))
);

create table main.grupoPT
(
    NAME VARCHAR2(100)
        constraint PK_grupoPT
            primary key,
    TYPE VARCHAR2(1),
    constraint CH_grupoPT_type
        check (TYPE IN ('C', 'U'))
);

create table main.grupoVidrio
(
    NAME text
        constraint PK_grupoVidrio
            primary key,
    TYPE text,
    constraint CH_grupoVidiro_type
        check (TYPE IN ('C', 'U'))
);

create table main.marco
(
    NAME         text
        constraint PK_marco
            primary key,
    GRUPO        text
        constraint FK_marco
            references main.grupoMarco,
    ABSORTIVIDAD NUMBER(5, 5),
    UMARCO       NUMBER(5, 5),
    TYPE         text,
    constraint CH_marco_type
        check (TYPE IN ('C', 'U'))
);

create table main.material
(
    NAME          text
        constraint PK_material
            primary key,
    THICKNESS     NUMBER(5, 5),
    CONDUCTIVITY  NUMBER(5, 5),
    DENSITY       NUMBER(5, 5),
    SPECIFIC_HEAT NUMBER(5, 5),
    VAPOUR_DF     NUMBER(5, 5),
    IMAGE         text,
    TYPE          text,
    GRUPO         text
        constraint FK_material
            references main.grupo,
    constraint CH_material_type
        check (TYPE IN ('C', 'U'))
);

create table main.compone
(
    NAME_CERR text
        constraint PK_compone_cerr
            references main.cerramiento,
    NAME_MAT  text
        constraint PK_compone_mat
            references main.material,
    ORDEN     NUMBER(5),
    THICKNESS NUMBER(5, 5),
    constraint PK_compone
        primary key (NAME_CERR, NAME_MAT, ORDEN)
);

create table main.sqlite_master
(
    type     TEXT,
    name     TEXT,
    tbl_name TEXT,
    rootpage INT,
    sql      TEXT
);

create table main.tipoFachada
(
    NAME VARCHAR2(100)
        constraint PK_tipoFachada
            primary key,
    TYPE VARCHAR2(1),
    constraint CH_PK_tipoFachada_type
        check (TYPE IN ('C', 'U'))
);

create table main.fachadaGrupo
(
    FACHADA VARCHAR2(100)
        constraint FK_fachadaGrupo2
            references main.tipoFachada,
    GRUPO   VARCHAR2(1)
        constraint FK_fachadaGrupo1
            references main.grupoPT,
    constraint PK_fachadaGrupo
        primary key (FACHADA, GRUPO)
);

create table main.puenteTermico
(
    NAME    VARCHAR2(100),
    FACHADA VARCHAR2(100)
        constraint FK_puenteTermico2
            references main.tipoFachada,
    FI      NUMBER(5, 5),
    IMAGE   VARCHAR2(200),
    TYPE    VARCHAR2(1),
    GRUPO   VARCHAR2(100)
        constraint FK_puenteTermico1
            references main.grupoPT,
    constraint PK_puenteTermico
        primary key (NAME, FACHADA, GRUPO),
    constraint CH_puenteTermico_type
        check (TYPE IN ('C', 'U'))
);

create table main.vidrio
(
    NAME        text
        constraint PK_vidiro
            primary key,
    GRUPO       text
        constraint FK_vidiro
            references main.grupoVidrio,
    FACTORSOLAR NUMBER(5, 5),
    UVIDRIO     NUMBER(5, 5),
    TYPE        text,
    constraint CH_vidiro_type
        check (TYPE IN ('C', 'U'))
);

