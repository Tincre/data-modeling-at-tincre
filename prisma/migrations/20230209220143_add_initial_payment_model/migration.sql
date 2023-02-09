-- CreateTable
CREATE TABLE "Payment" (
    "id" SERIAL NOT NULL,
    "paymentSentAt" TIMESTAMPTZ(6) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "myParam" TEXT,

    CONSTRAINT "Payment_pkey" PRIMARY KEY ("id")
);
