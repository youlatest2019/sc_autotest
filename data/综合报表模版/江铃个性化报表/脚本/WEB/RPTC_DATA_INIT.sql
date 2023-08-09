delete from DCAB_BS_BSPZ where BSPZBH in ('RPTC')
/
INSERT INTO DCAB_BS_BSPZ(BSPZBH,BSPZMC,JGJGID,ZXBSPL,PZ_SORT,RECALCULATE_FLAG) VALUES('RPTC','综合报表',1,1,50,1)
/
delete from dcab_bs_bsnr a where a.bspzbh='RPTC'
/
delete from dcab_bs_bsnr_dgroup where bspzbh='RPTC'
/


declare
  v_group_name varchar2(100);
  v_group_sort INTEGER;
  v_paramCnt    INTEGER;
  v_bspzbh      varchar2(20) := 'RPTC';
begin
      ---------------------------------------------------报送分组-----------------------------------------
v_group_name := '月报';
      v_group_sort := 0;
      select count(0) into v_paramCnt from dcab_bs_bsnr_dgroup where group_name = v_group_name and bspzbh = v_bspzbh;
      IF v_paramCnt = 0 THEN
          execute immediate 'insert into dcab_bs_bsnr_dgroup(id, group_name, group_sort, bspzbh) values(:1,:2,:3,:4)'
          using seq_dcab_bs_bsnr_dgroup.nextval, v_group_name, v_group_sort, v_bspzbh;
      ELSE
         execute immediate 'update dcab_bs_bsnr_dgroup set group_name=:1, group_sort=:2 where group_name=:3 and bspzbh=:4'
          using  v_group_name, v_group_sort, v_group_name, v_bspzbh;
        END IF;
v_group_name := '季报';
      v_group_sort := 1;
      select count(0) into v_paramCnt from dcab_bs_bsnr_dgroup where group_name = v_group_name and bspzbh = v_bspzbh;
      IF v_paramCnt = 0 THEN
          execute immediate 'insert into dcab_bs_bsnr_dgroup(id, group_name, group_sort, bspzbh) values(:1,:2,:3,:4)'
          using seq_dcab_bs_bsnr_dgroup.nextval, v_group_name, v_group_sort, v_bspzbh;
      ELSE
         execute immediate 'update dcab_bs_bsnr_dgroup set group_name=:1, group_sort=:2 where group_name=:3 and bspzbh=:4'
          using  v_group_name, v_group_sort, v_group_name, v_bspzbh;
        END IF;
v_group_name := '半年报';
      v_group_sort := 2;
      select count(0) into v_paramCnt from dcab_bs_bsnr_dgroup where group_name = v_group_name and bspzbh = v_bspzbh;
      IF v_paramCnt = 0 THEN
          execute immediate 'insert into dcab_bs_bsnr_dgroup(id, group_name, group_sort, bspzbh) values(:1,:2,:3,:4)'
          using seq_dcab_bs_bsnr_dgroup.nextval, v_group_name, v_group_sort, v_bspzbh;
      ELSE
         execute immediate 'update dcab_bs_bsnr_dgroup set group_name=:1, group_sort=:2 where group_name=:3 and bspzbh=:4'
          using  v_group_name, v_group_sort, v_group_name, v_bspzbh;
        END IF;		
v_group_name := '年报';
      v_group_sort := 3;
      select count(0) into v_paramCnt from dcab_bs_bsnr_dgroup where group_name = v_group_name and bspzbh = v_bspzbh;
      IF v_paramCnt = 0 THEN
          execute immediate 'insert into dcab_bs_bsnr_dgroup(id, group_name, group_sort, bspzbh) values(:1,:2,:3,:4)'
          using seq_dcab_bs_bsnr_dgroup.nextval, v_group_name, v_group_sort, v_bspzbh;
      ELSE
         execute immediate 'update dcab_bs_bsnr_dgroup set group_name=:1, group_sort=:2 where group_name=:3 and bspzbh=:4'
          using  v_group_name, v_group_sort, v_group_name, v_bspzbh;
        END IF;
end;
/
   insert into dcab_bs_bsnr(bsnrbh,bsnrmc,bspzbh,dgroup,bspl,valid_date,sfzdsb,nr_sort,holiday_flag)
   select 'PHJR01','PHJR01-普惠金融工作月报表','RPTC',
   (select i.id from dcab_bs_bsnr_dgroup i where i.group_name = '月报'  and i.bspzbh = 'RPTC' ),
   4,6.0,0,0,0
    from dual a
   where not exists (select * from dcab_bs_bsnr i where i.bsnrbh='PHJR01' or i.bsnrbh='PHJR01-YB')
/

   insert into dcab_bs_bsnr(bsnrbh,bsnrmc,bspzbh,dgroup,bspl,valid_date,sfzdsb,nr_sort,holiday_flag)
   select 'FXCJGZB01','FXCJGZB01-非现场监管关键指标','RPTC',
   (select i.id from dcab_bs_bsnr_dgroup i where i.group_name = '季报'  and i.bspzbh = 'RPTC' ),
   5,15.0,0,0,0
    from dual a
   where not exists (select * from dcab_bs_bsnr i where i.bsnrbh='FXCJGZB01' or i.bsnrbh='FXCJGZB01-JB')
/

   insert into dcab_bs_bsnr(bsnrbh,bsnrmc,bspzbh,dgroup,bspl,valid_date,sfzdsb,nr_sort,holiday_flag)
   select 'G4C00','G4C00-市场风险资本要求情况表','RPTC',
   (select i.id from dcab_bs_bsnr_dgroup i where i.group_name = '季报'  and i.bspzbh = 'RPTC' ),
   5,15.0,0,1,0
    from dual a
   where not exists (select * from dcab_bs_bsnr i where i.bsnrbh='G4C00' or i.bsnrbh='G4C00-JB')
/

   insert into dcab_bs_bsnr(bsnrbh,bsnrmc,bspzbh,dgroup,bspl,valid_date,sfzdsb,nr_sort,holiday_flag)
   select 'G3301','G3301-银行账簿利率风险计量报表(标准化计量框架简化版)','RPTC',
   (select i.id from dcab_bs_bsnr_dgroup i where i.group_name = '季报'  and i.bspzbh = 'RPTC' ),
   5,15.0,0,2,0
    from dual a
   where not exists (select * from dcab_bs_bsnr i where i.bsnrbh='G3301' or i.bsnrbh='G3301-JB')
/

   insert into dcab_bs_bsnr(bsnrbh,bsnrmc,bspzbh,dgroup,bspl,valid_date,sfzdsb,nr_sort,holiday_flag)
   select 'RZDB1','RZDB1-江西省银行业金融机构与融资担保公司担保贷款明细表','RPTC',
   (select i.id from dcab_bs_bsnr_dgroup i where i.group_name = '半年报'  and i.bspzbh = 'RPTC' ),
   6,15.0,0,0,0
    from dual a
   where not exists (select * from dcab_bs_bsnr i where i.bsnrbh='RZDB1' or i.bsnrbh='RZDB1-BNB')
/

   insert into dcab_bs_bsnr(bsnrbh,bsnrmc,bspzbh,dgroup,bspl,valid_date,sfzdsb,nr_sort,holiday_flag)
   select 'RZDB2','RZDB2-江西省银行业金融机构与融资担保公司担保贷款报表','RPTC',
   (select i.id from dcab_bs_bsnr_dgroup i where i.group_name = '半年报'  and i.bspzbh = 'RPTC' ),
   6,15.0,0,1,0
    from dual a
   where not exists (select * from dcab_bs_bsnr i where i.bsnrbh='RZDB2' or i.bsnrbh='RZDB2-BNB')
/

   insert into dcab_bs_bsnr(bsnrbh,bsnrmc,bspzbh,dgroup,bspl,valid_date,sfzdsb,nr_sort,holiday_flag)
   select 'T115','T115-绿色融资统计表','RPTC',
   (select i.id from dcab_bs_bsnr_dgroup i where i.group_name = '半年报'  and i.bspzbh = 'RPTC' ),
   6,15.0,0,2,0
    from dual a
   where not exists (select * from dcab_bs_bsnr i where i.bsnrbh='T115' or i.bsnrbh='T115-BNB')
/


--------------------报送内容分类 用于生成批次号-------------------------
declare cnt integer;
begin
  select count(0) into cnt from DCAB_BS_BSNR_TYPE a where a.id = 13;
  if cnt = 0 then
    execute immediate 'insert into DCAB_BS_BSNR_TYPE (ID, TYPE_NAME, TYPE_CODE) values (13, ''综合报表默认分类'', ''13'')';
  end if;
end;
/
update dcab_bs_bsnr set TYPE_ID = 13 where  bspzbh = 'RPTC'
/

