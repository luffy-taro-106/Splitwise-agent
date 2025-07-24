import { Box, Paper, Typography } from '@mui/material';

export default function Message({ message }) {
  const isUser = message.sender === 'user';

  return (
    <Box
      sx={{
        display: 'flex',
        justifyContent: isUser ? 'flex-end' : 'flex-start',
        width: '100%'
      }}
    >
      <Paper
        elevation={2}
        sx={{
          p: 2,
          maxWidth: '80%',
          bgcolor: isUser ? 'primary.main' : 'background.paper',
          color: isUser ? 'primary.contrastText' : 'text.primary',
          borderRadius: 2,
          borderBottomRightRadius: isUser ? 0 : 8,
          borderBottomLeftRadius: isUser ? 8 : 0,
        }}
      >
        <Typography variant="body1" sx={{ whiteSpace: 'pre-wrap' }}>
          {message.text}
        </Typography>
      </Paper>
    </Box>
  );
}
