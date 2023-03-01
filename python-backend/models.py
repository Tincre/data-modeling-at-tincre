from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    DateTime,
    Double,
    Integer,
    Numeric,
    PrimaryKeyConstraint,
    String,
    Table,
    Text,
    text,
)
from sqlalchemy.dialects.postgresql import OID, TIMESTAMP
from database import Base

metadata = Base.metadata


class Payment(Base):
    __tablename__ = "Payment"
    __table_args__ = (PrimaryKeyConstraint("id", name="Payment_pkey"),)

    id = Column(Integer)
    paymentSentAt = Column(
        TIMESTAMP(True, 6),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    )
    myParam = Column(Text)


class PrismaMigrations(Base):
    __tablename__ = "_prisma_migrations"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="_prisma_migrations_pkey"),
    )

    id = Column(String(36))
    checksum = Column(String(64), nullable=False)
    migration_name = Column(String(255), nullable=False)
    started_at = Column(
        DateTime(True), nullable=False, server_default=text("now()")
    )
    applied_steps_count = Column(
        Integer, nullable=False, server_default=text("0")
    )
    finished_at = Column(DateTime(True))
    logs = Column(Text)
    rolled_back_at = Column(DateTime(True))


t_pg_stat_statements = Table(
    "pg_stat_statements",
    metadata,
    Column("userid", OID),
    Column("dbid", OID),
    Column("toplevel", Boolean),
    Column("queryid", BigInteger),
    Column("query", Text),
    Column("plans", BigInteger),
    Column("total_plan_time", Double(53)),
    Column("min_plan_time", Double(53)),
    Column("max_plan_time", Double(53)),
    Column("mean_plan_time", Double(53)),
    Column("stddev_plan_time", Double(53)),
    Column("calls", BigInteger),
    Column("total_exec_time", Double(53)),
    Column("min_exec_time", Double(53)),
    Column("max_exec_time", Double(53)),
    Column("mean_exec_time", Double(53)),
    Column("stddev_exec_time", Double(53)),
    Column("rows", BigInteger),
    Column("shared_blks_hit", BigInteger),
    Column("shared_blks_read", BigInteger),
    Column("shared_blks_dirtied", BigInteger),
    Column("shared_blks_written", BigInteger),
    Column("local_blks_hit", BigInteger),
    Column("local_blks_read", BigInteger),
    Column("local_blks_dirtied", BigInteger),
    Column("local_blks_written", BigInteger),
    Column("temp_blks_read", BigInteger),
    Column("temp_blks_written", BigInteger),
    Column("blk_read_time", Double(53)),
    Column("blk_write_time", Double(53)),
    Column("temp_blk_read_time", Double(53)),
    Column("temp_blk_write_time", Double(53)),
    Column("wal_records", BigInteger),
    Column("wal_fpi", BigInteger),
    Column("wal_bytes", Numeric),
    Column("jit_functions", BigInteger),
    Column("jit_generation_time", Double(53)),
    Column("jit_inlining_count", BigInteger),
    Column("jit_inlining_time", Double(53)),
    Column("jit_optimization_count", BigInteger),
    Column("jit_optimization_time", Double(53)),
    Column("jit_emission_count", BigInteger),
    Column("jit_emission_time", Double(53)),
)


t_pg_stat_statements_info = Table(
    "pg_stat_statements_info",
    metadata,
    Column("dealloc", BigInteger),
    Column("stats_reset", DateTime(True)),
)
