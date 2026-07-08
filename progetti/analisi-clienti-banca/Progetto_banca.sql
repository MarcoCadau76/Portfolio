-- Inizializzazione database
use banca;

-- Esplorazione tabelle:

-- cliente: id_cliente, nome, cognome, data_nascita
select * from cliente limit 10;

-- conto: id_conto, id_cliente (-cliente), id_tipo_conto (-tipo-conto)
select * from conto limit 10;

-- tipo_conto:id_tipo_conto (-conto), desc_tipo_conto
select * from tipo_conto limit 10;

-- tipo_transazione: id_tipo_transazione(-transazioni), desc_tipo_transazione, segno
select * from tipo_transazione limit 10;

-- transazioni: data, id_tipo_transazioni(-tipo_transazione), id_conto(-conto)
select * from transazioni limit 10;

-- Creazione tabella feature clienti
drop table if exists banca.feature_clienti;
create table banca.feature_clienti as
select 
clt.id_cliente,
clt.nome,
clt.cognome,
clt.data_nascita,
TIMESTAMPDIFF(YEAR, clt.data_nascita, CURRENT_DATE()) eta,
round(sum(case when trn.importo >0 then importo else 0 end),2) tot_entrate,
round(sum(case when trn.importo <0 then importo else 0 end),2) tot_uscite,
count(case when trn.importo >0 then importo else null end) tot_operazioni_entrata,
count(case when trn.importo <0 then importo else null end) tot_operazioni_uscita,
count(distinct cnt.id_conto) num_conti,
count(distinct case when t_cnt.desc_tipo_conto = "Conto Base" then cnt.id_conto else null end) num_conto_base,
count(distinct case when t_cnt.desc_tipo_conto = "Conto Business" then cnt.id_conto else null end) num_conto_business,
count(distinct case when t_cnt.desc_tipo_conto = "Conto Privati" then cnt.id_conto else null end) num_conto_privati,
count(distinct case when t_cnt.desc_tipo_conto = "Conto Famiglie" then cnt.id_conto else null end) num_conto_famiglie,
round(sum(case when trn.importo >0 and t_cnt.desc_tipo_conto = "Conto Base" then importo else 0 end),2) tot_entrate_conto_base,
round(sum(case when trn.importo >0 and t_cnt.desc_tipo_conto = "Conto Business" then importo else 0 end),2) tot_entrate_conto_business,
round(sum(case when trn.importo >0 and t_cnt.desc_tipo_conto = "Conto Privati" then importo else 0 end),2) tot_entrate_conto_privati,
round(sum(case when trn.importo >0 and t_cnt.desc_tipo_conto = "Conto Famiglie" then importo else 0 end),2) tot_entrate_conto_famiglie,
round(sum(case when trn.importo <0 and t_cnt.desc_tipo_conto = "Conto Base" then importo else 0 end),2) tot_uscite_conto_base,
round(sum(case when trn.importo <0 and t_cnt.desc_tipo_conto = "Conto Business" then importo else 0 end),2) tot_uscite_conto_business,
round(sum(case when trn.importo <0 and t_cnt.desc_tipo_conto = "Conto Privati" then importo else 0 end),2) tot_uscite_conto_privati,
round(sum(case when trn.importo <0 and t_cnt.desc_tipo_conto = "Conto Famiglie" then importo else 0 end),2) tot_uscite_conto_famiglie,
count(case when trn.importo >0 and t_cnt.desc_tipo_conto = "Conto Base" then importo else null end) tot_operazioni_entrata_conto_base,
count(case when trn.importo >0 and t_cnt.desc_tipo_conto = "Conto Business" then importo else null end) tot_operazioni_entrata_conto_business,
count(case when trn.importo >0 and t_cnt.desc_tipo_conto = "Conto Privati" then importo else null end) tot_operazioni_entrata_conto_privati,
count(case when trn.importo >0 and t_cnt.desc_tipo_conto = "Conto Famiglie" then importo else null end) tot_operazioni_entrata_conto_famiglia,
count(case when trn.importo <0 and t_cnt.desc_tipo_conto = "Conto Base" then importo else null end) tot_operazioni_uscita_conto_base,
count(case when trn.importo <0 and t_cnt.desc_tipo_conto = "Conto Business" then importo else null end) tot_operazioni_uscita_conto_business,
count(case when trn.importo <0 and t_cnt.desc_tipo_conto = "Conto Privati" then importo else null end) tot_operazioni_uscita_conto_privati,
count(case when trn.importo <0 and t_cnt.desc_tipo_conto = "Conto Famiglie" then importo else null end) tot_operazioni_uscita_conto_famiglia
from cliente clt
join conto cnt on clt.id_cliente = cnt.id_cliente
join transazioni trn on cnt.id_conto = trn.id_conto
join tipo_conto t_cnt on cnt.id_tipo_conto = t_cnt.id_tipo_conto
group by 1,2,3,4
order by tot_entrate desc;

-- Verifica risultato
select * from banca.feature_clienti limit 10;
