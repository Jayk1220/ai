-- E:/ai/source/01_python/ch15.sql
-- 테이블 생성 (NAME, TEL, EMAIL, AGE, GRADE, ETC)
DROP TABLE MEMBER;
CREATE TABLE MEMBER(
    NAME    VARCHAR2(20),
    TEL     VARCHAR2(20),
    EMAIL   VARCHAR(20) UNIQUE, 
    AGE     NUMBER(3),
    GREADE  NUMBER(1),
    ETC     VARCHAR2(100)
);

--     1번 입력
INSERT INTO MEMBER VALUES ('홍길동','010-9999-9999','H@H.COM',33, 2, '까칠');

-- 2번 전체조회, 5번 CSV 내보내기
SELECT * FROM MEMBER ORDER BY NAME;

-- 3번 이름조회

SELECT * FROM MEMBER WHERE NAME = '홍길동';

-- 4 삭제
DELETE FROM MEMBER WHERE EMAIL='H@H.COM';

select * from member;

COMMIT;