## Note

The application successfully connects to Binance Demo/Testnet public endpoints.

Public endpoint test:

GET /fapi/v1/ping -> {}

Authenticated requests currently return:

APIError(code=-2015): Invalid API-key, IP, or permissions for action

The application correctly performs request signing, input validation, CLI parsing, structured logging, and graceful error handling.