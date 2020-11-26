--1. Record label
CREATE TABLE recordLabel(
    companyName text,
    dateEstablished date,
    labelLocation text,
    recordLabelId bigint not null,
    PRIMARY KEY (recordLabelId)
);
-- 2. Publishes
CREATE TABLE publishes(
    albumId bigint not null,
    recordLabelId bigint not null,
    PRIMARY KEY (albumId, recordLabelId)
);
--3. artist
CREATE TABLE artist(
    artistId bigint not null,
    artistName text,
    age integer,
    PRIMARY KEY (artistId)
);
--4. musician
CREATE TABLE musician(
    artistId bigint not null,
    musicianId bigint not null,
    instrument text,
    band text,
    PRIMARY KEY (artistId, musicianId)
);
--5. Played
CREATE TABLE played(
    albumId bigint not null,
    musicianId bigint not null,
    PRIMARY KEY (albumId, musicianId)
);
--6. album
CREATE TABLE album(
    albumDuration integer,
    albumId bigint not null,
    title text,
    coverArtURL text,
    PRIMARY KEY (albumId)
);
--7. song
CREATE TABLE song(
    title text,
    genre text,
    songDuration integer,
    songId bigint not null,
    sourceLink text,
    releaseYear integer,
    PRIMARY KEY (songId)
);
--8. Contains
CREATE TABLE contains(
    albumId bigint not null,
    songId bigint not null,
    PRIMARY KEY (songId, albumId)
);
--9. made
CREATE TABLE made(
    knownFor text,
    albumId bigint not null,
    artistId bigint not null,
    PRIMARY KEY (albumId, artistId),
    FOREIGN KEY (albumId) REFERENCES album(albumId),
    FOREIGN KEY (artistId) REFERENCES artist(artistId)
);
--10. Rating
CREATE TABLE rating(
    numOfRating integer,
    averageRating decimal,
    userRating integer,
    albumId bigint not null,
    songId bigint not null,
    PRIMARY KEY (albumId, songId),
    FOREIGN KEY (songId) REFERENCES song(songId),
    FOREIGN KEY (albumId) REFERENCES album(albumId)
);