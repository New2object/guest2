drop table if exists defects;
create table defects (
  id integer primary key autoincrement,
  title text not null,
  content text not null,
  author text,
  tag_id integer
);

drop table if exists tags;
create table tags (
  id integer primary key autoincrement,
  title text not null,
  type text not null,
  description text not null
);

insert into tags values(1, 'Bug', 'danger', '确定是bug');
insert into tags values(2, '验证通过', 'default', '验证通过，关闭');
insert into tags values(3, '体验问题', 'warning', '用户体验有问题');

insert into defects values(1, '前端没有做校验', '如题', 'root', 1);
insert into defects values(2, 'content不能为空', '如题', 'root', 3);
