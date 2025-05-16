-- 선택한 테이블에 있는 데이터를 모두 보여달라는 명령어
select * from emp;

-- 선택한 테이블에 있는 데이터가 전체 몇 건인지 확인하는 명령여
select count(*) from emp;

-- 선택한 테이블의 선택한 필드명의 데이터만 보여달라는 명령어
select empno, ename, job from emp;

-- ailasing - 별명을 의미하며 테이블명을 수정해서 부를 수 있음
select empno , ename , job
from emp as e;

select e.empno , e.ename , e.job
from emp as e;

/*
Null 값은 DB 에서는 '알수없는' 의 의미이며
파이썬에서는 'None' 과 같고 수학적으로 무한대의 의미를 가짐
*/

select empno , sal , comm , sal+ifnull(comm , 0)
from emp;

/*
홍길동의 급여는 얼마입니다. 
*/
select concat(ename , "님의 급여는" , sal , "입니다.") as title
from emp;

/*
select 필드명
from 테이블명
where 조건절

선택한 테이블과 필드에서 조건절을 만족시키는 데이터만 출력
*/

select *
from emp
where ename = "smith";

# 이름이 smith 이거나 ford 인 사람
select *
from emp
where ename = "smith" or ename = "ford";

/*
급여가 3,000 이상인 사원의 이름과 급여를 조회하시오
직무가 'MANAGER' 인 사람의 정보를 조회하시오
급여가 2,000 이상 5,000 이하인 사원을 조회하시오
커미션이 Null 이 아닌 사원을 조회하시오
'A' 로 시작하는 이름을 가진 사원을 조회하시오
부서번호가 10, 20, 30 에 해당하는 사원을 조회하시오
급여가 1000 미만이거나 커미션이 500 초과인 사원을 조회하시오
관리자가 없는 사원(mgr 이 null) 을 조회하시오
직무가 Clerk 이면서 부서번호가 20 인 사원을 조회하시오
입사일이 1981 이전인 사원을 조회하시오



*/
# 급여가 3,000 이상인 사원의 이름과 급여를 조회하시오
select e.ename , e.sal
from emp as e
where sal >= 3000;

# 직무가 'MANAGER' 인 사람의 정보를 조회하시오
select *
from emp
where job = "manager";

# 급여가 2000 이상 5000 이하인 사원을 조회하시오
select *
from emp
where sal >= 2000 and sal <= 5000;

# 커미션이 Null 이 아닌 사원을 조회하시오
select *
from emp
where comm is not null;

# "A" 로 시작하는 이름을 가진 사원을 조회하시오
select *
from emp
where ename like "a%";

# 부서번호가 10 , 20 , 30 인 사원을 조회하시오
select *
from emp
where deptno = "10" or deptno = "20" or deptno = "30";

select *
from emp
where deptno in (10,20,30);

select *
from emp
where empno in (7521,7565,7903,7934);

# 급여가 1000 미만이거나 커미션이 500 초과인 사람만 조회하시오
select *
from emp
where sal < 1000 or comm > 500;

# 관리자가 없는 사원(mgr 이 null) 을 조회하시오
select *
from emp
where mgr is null;

# 직무가 Clerk 이면서 부서번호가 20 인 사원을 조회하시오
select *
from emp
where job = "clerk" and deptno ="20";

# 입사일이 1981 이전인 사원을 조회하시오
select *
from emp
where hiredate < "1981-01-01";

select *
from emp
order by ename;