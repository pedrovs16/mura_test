// components/ReceiveEmailButton.tsx
import * as React from "react";
import { useState, ChangeEvent } from "react";
import { Button, useNotify, useDataProvider } from "react-admin";
import {
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  TextField as MuiTextField,
} from "@mui/material";

const ReceiveEmailButton = () => {
  const notify = useNotify();
  const dataProvider = useDataProvider();
  const [open, setOpen] = useState(false);
  const [formData, setFormData] = useState({
    address: "",
    to: "",
    subject: "",
    body: "",
    sent_at: new Date().toISOString(),
    reply_to: "",
  });

  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);

  const handleChange = (
    event: ChangeEvent<HTMLInputElement | HTMLTextAreaElement>
  ) => {
    setFormData({
      ...formData,
      [event.target.name]: event.target.value,
    });
  };

  const handleSubmit = async () => {
    try {
      await dataProvider.create("emails/receive", { data: formData });
      notify("Email received successfully", { type: "info" });
      handleClose();
    } catch (error) {
      notify("Error receiving email", { type: "error" });
    }
  };

  const formatDateForInput = (dateStr: string) => {
    return dateStr ? dateStr.substring(0, 16) : "";
  };

  return (
    <>
      <Button label="Receive Email" onClick={handleOpen} />
      <Dialog open={open} onClose={handleClose}>
        <DialogTitle>Receive Email</DialogTitle>
        <DialogContent>
          <MuiTextField
            margin="dense"
            name="address"
            label="Sender Email"
            fullWidth
            required
            value={formData.address}
            onChange={handleChange}
          />
          <MuiTextField
            margin="dense"
            name="to"
            label="Recipient Email"
            fullWidth
            required
            value={formData.to}
            onChange={handleChange}
          />
          <MuiTextField
            margin="dense"
            name="subject"
            label="Subject"
            fullWidth
            required
            value={formData.subject}
            onChange={handleChange}
          />
          <MuiTextField
            margin="dense"
            name="body"
            label="Email Body"
            fullWidth
            multiline
            required
            value={formData.body}
            onChange={handleChange}
          />
          <MuiTextField
            margin="dense"
            name="sent_at"
            label="Sent At"
            type="datetime-local"
            fullWidth
            required
            value={formatDateForInput(formData.sent_at)}
            onChange={handleChange}
          />
          <MuiTextField
            margin="dense"
            name="reply_to"
            label="Reply To"
            fullWidth
            value={formData.reply_to}
            onChange={handleChange}
          />
        </DialogContent>
        <DialogActions>
          <Button label="Cancel" onClick={handleClose} />
          <Button label="Submit" onClick={handleSubmit} />
        </DialogActions>
      </Dialog>
    </>
  );
};

export default ReceiveEmailButton;
